from django.urls import path
from . import views

urlpatterns = [
    # articles/ 경로에 GET or POST 요청이 왔을 때, 행위 method에 따라 서로 다른 작업 진행
    path('', views.article_get_or_create),
]
