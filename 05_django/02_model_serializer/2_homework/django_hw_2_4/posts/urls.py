from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_get_or_create),
    path('<int:post_pk>/', views.post_detail),
    # path('', views.post_handler),
]
