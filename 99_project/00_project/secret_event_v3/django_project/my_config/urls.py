
from django.contrib import admin
from django.urls import path
from letters import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('letters/', views.letters_list),
    # path('letters/<int:id>', views.choose_letter)
]
