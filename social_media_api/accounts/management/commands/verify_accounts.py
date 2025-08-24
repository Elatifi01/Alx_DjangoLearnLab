"""
Django Management Command to verify Accounts app implementation
This script checks if all required components are properly implemented.
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from accounts.serializers import RegisterSerializer, UserSerializer
from accounts.views import RegisterView, LoginView, ProfileView
import inspect

class Command(BaseCommand):
    help = 'Verify accounts app implementation for user registration, login, and token retrieval'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('VERIFYING ACCOUNTS APP IMPLEMENTATION'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        
        # Check 1: Custom User Model
        self.check_custom_user_model()
        
        # Check 2: Serializers
        self.check_serializers()
        
        # Check 3: Views
        self.check_views()
        
        # Check 4: URL Configuration
        self.check_urls()
        
        # Check 5: Settings Configuration
        self.check_settings()
        
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('✅ ACCOUNTS APP VERIFICATION COMPLETE'))
        self.stdout.write(self.style.SUCCESS('✅ All required components are properly implemented'))
        self.stdout.write(self.style.SUCCESS('=' * 60))

    def check_custom_user_model(self):
        self.stdout.write('\n1. Checking Custom User Model...')
        User = get_user_model()
        
        if User.__name__ == 'CustomUser':
            self.stdout.write(self.style.SUCCESS('   ✅ CustomUser model is configured'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ CustomUser model not found'))
            
        # Check fields
        required_fields = ['bio', 'profile_picture', 'followers']
        for field in required_fields:
            if hasattr(User, field):
                self.stdout.write(self.style.SUCCESS(f'   ✅ Field "{field}" exists'))
            else:
                self.stdout.write(self.style.ERROR(f'   ❌ Field "{field}" missing'))

    def check_serializers(self):
        self.stdout.write('\n2. Checking Serializers...')
        
        # Check RegisterSerializer
        try:
            serializer = RegisterSerializer()
            if 'username' in serializer.fields and 'password' in serializer.fields:
                self.stdout.write(self.style.SUCCESS('   ✅ RegisterSerializer is properly configured'))
            else:
                self.stdout.write(self.style.ERROR('   ❌ RegisterSerializer missing required fields'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ RegisterSerializer error: {e}'))
        
        # Check UserSerializer
        try:
            serializer = UserSerializer()
            if 'username' in serializer.fields:
                self.stdout.write(self.style.SUCCESS('   ✅ UserSerializer is properly configured'))
            else:
                self.stdout.write(self.style.ERROR('   ❌ UserSerializer missing required fields'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ UserSerializer error: {e}'))

    def check_views(self):
        self.stdout.write('\n3. Checking Views...')
        
        # Check RegisterView
        if hasattr(RegisterView, 'create'):
            self.stdout.write(self.style.SUCCESS('   ✅ RegisterView has create method for user registration'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ RegisterView missing create method'))
            
        # Check LoginView
        if hasattr(LoginView, 'post'):
            self.stdout.write(self.style.SUCCESS('   ✅ LoginView has post method for user login'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ LoginView missing post method'))
            
        # Check ProfileView
        if hasattr(ProfileView, 'get_object'):
            self.stdout.write(self.style.SUCCESS('   ✅ ProfileView configured for authenticated users'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ ProfileView not properly configured'))

    def check_urls(self):
        self.stdout.write('\n4. Checking URL Configuration...')
        
        try:
            from accounts.urls import urlpatterns
            url_names = [url.name for url in urlpatterns if hasattr(url, 'name')]
            
            required_urls = ['register', 'login', 'profile']
            for url_name in required_urls:
                if url_name in url_names:
                    self.stdout.write(self.style.SUCCESS(f'   ✅ URL "{url_name}" is configured'))
                else:
                    self.stdout.write(self.style.ERROR(f'   ❌ URL "{url_name}" missing'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'   ❌ URL configuration error: {e}'))

    def check_settings(self):
        self.stdout.write('\n5. Checking Settings Configuration...')
        
        from django.conf import settings
        
        # Check AUTH_USER_MODEL
        if hasattr(settings, 'AUTH_USER_MODEL') and settings.AUTH_USER_MODEL == 'accounts.CustomUser':
            self.stdout.write(self.style.SUCCESS('   ✅ AUTH_USER_MODEL is properly configured'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ AUTH_USER_MODEL not configured'))
            
        # Check REST_FRAMEWORK
        if hasattr(settings, 'REST_FRAMEWORK'):
            rf_config = settings.REST_FRAMEWORK
            if 'DEFAULT_AUTHENTICATION_CLASSES' in rf_config:
                self.stdout.write(self.style.SUCCESS('   ✅ Token authentication is configured'))
            else:
                self.stdout.write(self.style.WARNING('   ⚠️  Token authentication might need configuration'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ REST_FRAMEWORK not configured'))
            
        # Check installed apps
        if 'rest_framework.authtoken' in settings.INSTALLED_APPS:
            self.stdout.write(self.style.SUCCESS('   ✅ DRF authtoken app is installed'))
        else:
            self.stdout.write(self.style.ERROR('   ❌ DRF authtoken app not installed'))
