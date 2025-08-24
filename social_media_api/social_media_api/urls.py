"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.urls import include  # Import include to use it for including other URL configurations
from django.http import JsonResponse


def api_root(request):
    """Root API endpoint that lists all available endpoints"""
    return JsonResponse({
        'message': 'Welcome to Social Media API',
        'endpoints': {
            'admin': '/admin/',
            'posts': '/api/posts/',
            'accounts': '/api/accounts/',
            'notifications': '/api/notifications/',
        },
        'version': '1.0'
    })


urlpatterns = [
    path('', api_root, name='api-root'),  # Root endpoint
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),  # Include the URLs from the posts app
    path('api/accounts/', include('accounts.urls')),  # Include the URLs from the accounts app
    path('api/notifications/', include('notifications.urls')),  # Include the URLs from the notifications app
]


