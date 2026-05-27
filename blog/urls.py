from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка — список постів
    path('', views.index, name='index'),
    
    # Сторінка окремого поста (з його унікальним ID)
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    
    # Сторінка створення нового поста
    path('new/', views.post_new, name='post_new'),
]