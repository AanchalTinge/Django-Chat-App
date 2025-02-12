from django.urls import path, include
from django.contrib import admin
from chat import views  # Import views from your chat app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # Include chat app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Add authentication URLs
    path('accounts/profile/', views.profile, name='profile'),  # Add a profile URL
    path('signup/', views.signup, name='signup'),  # Add a signup URL
    path('', views.home, name='home'),  # Add a view for the root URL
]