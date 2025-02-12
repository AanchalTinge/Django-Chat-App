from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),  # Root URL for the chat app
    path('room/<int:receiver_id>/', views.chat_room, name='chat_room'),
]