import base64
from io import BytesIO

import matplotlib.pyplot as plt
import torch
from django.shortcuts import render
from PIL import Image, ImageDraw

from .forms import ImageUploadForm

# YOLOv5 모델 로드 (서버 시작 시 한 번만 로드)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)  # yolov5s

def main_page(request):
    return render(request, 'main_page.html')

def detect_objects(request):
    if request.method == 'POST' and 'image' in request.FILES:
        try:
            # 업로드된 이미지 처리
            uploaded_image = request.FILES['image']
            image = Image.open(uploaded_image)

            # YOLOv5 모델을 사용하여 객체 탐지 수행
            results = model(image)

            # 탐지된 객체 정보 가져오기
            detected_objects = results.pandas().xywh[0].to_dict(orient="records")

            # 객체 종류별로 개수 세기 (라벨별 통계)
            object_counts = {}
            for obj in detected_objects:
                label = obj['name']
                object_counts[label] = object_counts.get(label, 0) + 1

            # 그래프 생성
            fig, ax = plt.subplots()
            ax.bar(object_counts.keys(), object_counts.values())
            ax.set_xlabel('Object Classes')
            ax.set_ylabel('Count')
            ax.set_title('Object Detection Counts')

            # 그래프 이미지를 바이트로 변환
            chart_byte_arr = BytesIO()
            plt.savefig(chart_byte_arr, format='PNG')
            chart_byte_arr.seek(0)

            # 그래프 이미지를 base64로 인코딩
            chart_base64 = base64.b64encode(chart_byte_arr.read()).decode('utf-8')

            # 이미지 시각화 (사각형 그리기)
            draw = ImageDraw.Draw(image)
            for obj in detected_objects:
                # 객체의 좌표와 크기 (xcenter, ycenter, width, height)
                xcenter = obj['xcenter']
                ycenter = obj['ycenter']
                width = obj['width']
                height = obj['height']

                # 좌측 상단과 우측 하단 좌표 계산
                left = xcenter - width / 2
                top = ycenter - height / 2
                right = xcenter + width / 2
                bottom = ycenter + height / 2

                # 사각형 그리기
                draw.rectangle([left, top, right, bottom], outline="red", width=3)

                # 객체 이름과 confidence 표시
                label = f"{obj['name']} {obj['confidence']:.2f}"
                draw.text((left, top - 10), label, fill="red")

            # 결과 이미지를 웹에서 표시할 수 있도록 바이트로 변환
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)

            # 이미지를 base64로 변환 (웹에서 표시할 수 있게)
            img_base64 = base64.b64encode(img_byte_arr.read()).decode('utf-8')

            # 템플릿에 결과 전달
            return render(request, 'index.html', {
                'img_base64': img_base64,       # 탐지된 이미지
                'chart_base64': chart_base64,   # 객체 카운트 그래프
                'form': ImageUploadForm()       # 업로드 폼
            })

        except Exception as e:
            # 예외 처리: 업로드된 파일이 이미지가 아닌 경우나 다른 오류가 발생할 때
            return render(request, 'index.html', {
                'error': str(e),  # 에러 메시지를 화면에 표시
                'form': ImageUploadForm()  # 업로드 폼
            })

    # GET 요청 시 빈 폼 반환
    return render(request, 'index.html', {'form': ImageUploadForm()})
