import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
django.setup()

from accounts.models import CustomUser

try:
    # Get all users
    all_users = CustomUser.objects.all()
    total_users = all_users.count()
    
    # Get superusers
    superusers = CustomUser.objects.filter(is_superuser=True)
    superuser_count = superusers.count()
    
    print(f"Total users in database: {total_users}")
    print(f"Superusers: {superuser_count}")
    
    if total_users > 0:
        print("\nExisting users:")
        for user in all_users:
            print(f"- Username: {user.username}, Email: {user.email}, Superuser: {user.is_superuser}")
    
    if superuser_count == 0:
        print("\n❌ No superuser found. You need to create one.")
        print("Run: python manage.py createsuperuser")
    else:
        print(f"\n✅ {superuser_count} superuser(s) found.")
        
except Exception as e:
    print(f"Error checking users: {e}")
