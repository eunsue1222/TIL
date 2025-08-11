"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# articles app이 가지고 있는 views 모듈
# from articles import views
# from accounts import views

# 프로젝트가 커지면 include라는 기능을 사용해 app마다 경로를 따로 관리

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'articles/' 라는 경로로 요청이 오면, 요청은 articles 앱이 가진 urls가 처리
    path('articles/', include('articles.urls'))

    # # 사용자가 index 라는 경로 (상대경로)로 요청을 보내면, views에 있는 index 함수를 실행시킨다.
    # path('index/', views.index),
    # # variable routing
    # # 경로에 사용자가 적은 값을 변수에 담기 -> <변수명>
    # # path('article/<variable_name>/', views.detail),
    # path('article/<int:article_pk>/', views.detail),
    # path('accounts/login/', )
]
