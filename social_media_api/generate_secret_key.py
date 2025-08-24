#!/usr/bin/env python
"""
Script to generate a new Django SECRET_KEY
Run this script to get a new secure secret key for your Django project.
"""

import os
import django
from django.core.management.utils import get_random_secret_key

def generate_secret_key():
    """Generate a new Django secret key"""
    return get_random_secret_key()

if __name__ == "__main__":
    new_key = generate_secret_key()
    print("=" * 60)
    print("NEW DJANGO SECRET KEY GENERATED")
    print("=" * 60)
    print(f"SECRET_KEY = '{new_key}'")
    print("=" * 60)
    print("INSTRUCTIONS:")
    print("1. Copy the SECRET_KEY above")
    print("2. Replace it in your settings.py file")
    print("3. Or add it to your .env file as DJANGO_SECRET_KEY")
    print("4. Keep this key secure and never commit it to version control!")
    print("=" * 60)
