from django.contrib import admin
from django.urls import path

from app import views  # app에서 views 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),  # 메인 페이지 URL
    path('yolov5/', views.detect_objects, name='detect_objects'),  # YOLOv5 객체 탐지 페이지 URL
]