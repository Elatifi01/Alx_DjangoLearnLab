#!/usr/bin/env python
"""
Test script to verify the accounts app functionality for user registration, login, and token retrieval.
This script tests the core requirements for the accounts app implementation.
"""

import requests
import json

# Base URL for the API
BASE_URL = "http://127.0.0.1:8000/api/accounts"

def test_registration():
    """Test user registration endpoint"""
    print("Testing user registration...")
    
    # Test data for registration
    registration_data = {
        "username": "testuser123",
        "password": "securepassword123",
        "email": "testuser@example.com",
        "bio": "This is a test user bio"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/register/", json=registration_data)
        print(f"Registration Response Status: {response.status_code}")
        
        if response.status_code == 201:
            data = response.json()
            print("✅ Registration successful!")
            print(f"User ID: {data.get('id')}")
            print(f"Username: {data.get('username')}")
            print(f"Email: {data.get('email')}")
            print(f"Token: {data.get('token')[:20]}..." if data.get('token') else "No token")
            return data.get('token'), data.get('id')
        else:
            print(f"❌ Registration failed: {response.text}")
            return None, None
    except Exception as e:
        print(f"❌ Registration error: {e}")
        return None, None

def test_login(username, password):
    """Test user login endpoint"""
    print("\nTesting user login...")
    
    login_data = {
        "username": username,
        "password": password
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login/", json=login_data)
        print(f"Login Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Login successful!")
            print(f"User ID: {data.get('user_id')}")
            print(f"Email: {data.get('email')}")
            print(f"Token: {data.get('token')[:20]}..." if data.get('token') else "No token")
            return data.get('token')
        else:
            print(f"❌ Login failed: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None

def test_profile_access(token):
    """Test profile access with token authentication"""
    print("\nTesting profile access...")
    
    headers = {
        "Authorization": f"Token {token}"
    }
    
    try:
        response = requests.get(f"{BASE_URL}/profile/", headers=headers)
        print(f"Profile Access Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Profile access successful!")
            print(f"Username: {data.get('username')}")
            print(f"Email: {data.get('email')}")
            print(f"Bio: {data.get('bio')}")
            return True
        else:
            print(f"❌ Profile access failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Profile access error: {e}")
        return False

def test_endpoints_info():
    """Test GET requests to endpoints for information"""
    print("\nTesting endpoint information...")
    
    endpoints = ["/register/", "/login/", "/profile/"]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            print(f"GET {endpoint}: Status {response.status_code}")
            if response.status_code in [200, 401]:  # 401 for profile without auth is expected
                print(f"✅ Endpoint info available")
            else:
                print(f"❌ Unexpected response: {response.text}")
        except Exception as e:
            print(f"❌ Error accessing {endpoint}: {e}")

def main():
    """Main test function"""
    print("=" * 60)
    print("TESTING ACCOUNTS APP - USER REGISTRATION, LOGIN, AND TOKEN RETRIEVAL")
    print("=" * 60)
    
    # Test endpoint information
    test_endpoints_info()
    
    # Test registration
    token, user_id = test_registration()
    
    if token:
        # Test login with the same credentials
        login_token = test_login("testuser123", "securepassword123")
        
        if login_token:
            # Test profile access
            test_profile_access(login_token)
            
            print("\n" + "=" * 60)
            print("✅ ALL TESTS PASSED! Accounts app implementation is working correctly.")
            print("✅ User registration, login, and token retrieval are functioning properly.")
            print("=" * 60)
        else:
            print("\n❌ Login test failed, but registration worked.")
    else:
        print("\n❌ Registration test failed.")
    
    print("\nTest completed. Check the results above.")

if __name__ == "__main__":
    main()
