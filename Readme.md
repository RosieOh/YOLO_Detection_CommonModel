# YOLOv5 Object Detection 프로젝트 설정 및 실행 가이드


## 🧑‍🦲 팀원(가나다순)

<table>
  <tbody>
    <tr>
            <td align="center"><a href="https://github.com/RosieOh"><img src="https://avatars.githubusercontent.com/u/104690434?v=4" width="100px;" alt=""/><br /><sub><b>오태훈</b></sub></a><br /><sub><b>개발</b></sub></td>
      <td align="center"><a href="https://github.com/RosieOh"><img src="https://github.com/SP0F0/.github/assets/62829894/fc0c73b5-3bdc-4edf-8c7f-b7b8eff9bf67" width="100px;" alt=""/><br /><sub><b>김경엽</b></sub></a><br /><sub><b>개발</b></sub></td>
    </tr>
  </tbody>
</table>

<br/>
<hr/>
<br/>

> 1. 프로젝트 소개
이 프로젝트는 YOLOv5를 사용하여 이미지에서 객체를 탐지하고, 그 결과를 웹 페이지에서 시각화하는 Django 웹 애플리케이션입니다. 업로드된 이미지를 YOLOv5 모델을 통해 분석하고, 그 결과를 웹 페이지에 표시합니다.

<br/>
<hr/>
<br/>

> 2. 프로젝트 실행을 위한 환경 설정
이 문서는 프로젝트를 다른 개발 환경에서 실행할 수 있도록 필요한 의존성 패키지를 설치하고 프로젝트를 실행하는 방법을 설명합니다.

<br/>
<hr/>
<br/>

> 3. 필요한 패키지 설치
 - 3.1. 가상 환경 설정 (선택사항)
프로젝트의 의존성을 관리하고 충돌을 방지하기 위해 가상 환경을 사용하는 것이 좋습니다.

<br/>
<hr/>
<br/>

> 가상 환경 생성 (만약 venv 또는 conda를 사용한다면):
 - venv를 사용할 경우:
```bash
python -m venv venv
```


 - conda를 사용할 경우:
``` bash
conda create --name yolov5_env python=3.8
conda activate yolov5_env
```

 - 3.2. 의존성 패키지 설치
프로젝트가 사용하는 모든 패키지들을 requirements.txt 파일에 명시해두었습니다. 이 파일을 기반으로 필요한 패키지를 설치할 수 있습니다.

#### requirements.txt 파일 실행

```bash
pip install -r requirements.txt
```

> 4. 프로젝트 실행
 - 4.1. Django 서버 실행
 Django 프로젝트 디렉토리로 이동 터미널에서 Django 프로젝트의 루트 디렉토리로 이동합니다.

``` bash
cd /path/to/your/project
```

``` bash
python manage.py runserver
```

```bash
http://127.0.0.1:8000/
```
