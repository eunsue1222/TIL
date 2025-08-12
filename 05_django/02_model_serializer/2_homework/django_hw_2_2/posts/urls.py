from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_get_or_create),
]