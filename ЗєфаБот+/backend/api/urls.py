from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_handler, name='chat_api'),
    path('clear_mem/', views.clear_memory, name='clear_mem_api'),
]
