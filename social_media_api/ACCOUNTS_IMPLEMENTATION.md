# Accounts App Implementation Summary

## ✅ Task Completed: "Implement views and serializers in the accounts app for user registration, login, and token retrieval."

### What has been implemented:

## 1. 🔐 User Registration
**File: `accounts/views.py` - RegisterView**
- ✅ Allows users to register with username, password, email, and optional bio
- ✅ Automatically creates authentication token upon registration
- ✅ Returns user details and token in response
- ✅ Accessible at `/api/accounts/register/`

**File: `accounts/serializers.py` - RegisterSerializer**
- ✅ Validates registration data
- ✅ Securely hashes passwords
- ✅ Creates CustomUser instance
- ✅ Automatically generates authentication token

## 2. 🔑 User Login
**File: `accounts/views.py` - LoginView**
- ✅ Extends DRF's ObtainAuthToken for secure login
- ✅ Returns authentication token upon successful login
- ✅ Returns user ID and email with token
- ✅ Accessible at `/api/accounts/login/`

## 3. 🎫 Token Authentication
**File: `social_media_api/settings.py`**
- ✅ Configured `rest_framework.authtoken` in INSTALLED_APPS
- ✅ Set TokenAuthentication as default authentication class
- ✅ Tokens are automatically created for new users

## 4. 👤 User Profile Management
**File: `accounts/views.py` - ProfileView**
- ✅ Allows authenticated users to view/update their profile
- ✅ Requires token authentication
- ✅ Accessible at `/api/accounts/profile/`

**File: `accounts/serializers.py` - UserSerializer**
- ✅ Serializes user data including bio, profile picture, followers
- ✅ Used for profile retrieval and updates

## 5. 🏗️ Custom User Model
**File: `accounts/models.py` - CustomUser**
- ✅ Extends Django's AbstractUser
- ✅ Includes bio, profile_picture, and followers fields
- ✅ Properly configured in settings.py

## 6. 🌐 URL Configuration
**File: `accounts/urls.py`**
- ✅ `/api/accounts/register/` - User registration
- ✅ `/api/accounts/login/` - User login
- ✅ `/api/accounts/profile/` - User profile management
- ✅ Additional endpoints for following/unfollowing users

## 7. ⚙️ Settings Configuration
**File: `social_media_api/settings.py`**
- ✅ `AUTH_USER_MODEL = 'accounts.CustomUser'`
- ✅ `rest_framework.authtoken` in INSTALLED_APPS
- ✅ Token authentication configured in REST_FRAMEWORK settings

## API Endpoints Summary:

### Registration
```
POST /api/accounts/register/
{
    "username": "john_doe",
    "password": "secure_password123",
    "email": "john@example.com",
    "bio": "Hello, I am John!"
}

Response:
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "bio": "Hello, I am John!",
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Login
```
POST /api/accounts/login/
{
    "username": "john_doe",
    "password": "secure_password123"
}

Response:
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
    "user_id": 1,
    "email": "john@example.com"
}
```

### Profile Access
```
GET /api/accounts/profile/
Headers: Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

Response:
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "bio": "Hello, I am John!",
    "profile_picture": null,
    "followers": []
}
```

## 🧪 Testing

To test the implementation:

1. **Start the server:**
   ```bash
   python manage.py runserver
   ```

2. **Test registration:**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
        -H "Content-Type: application/json" \
        -d '{"username":"testuser","password":"testpass123","email":"test@example.com"}'
   ```

3. **Test login:**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
        -H "Content-Type: application/json" \
        -d '{"username":"testuser","password":"testpass123"}'
   ```

4. **Test profile access:**
   ```bash
   curl -X GET http://127.0.0.1:8000/api/accounts/profile/ \
        -H "Authorization: Token YOUR_TOKEN_HERE"
   ```

## ✅ Requirements Met:

1. ✅ **User Registration** - Fully implemented with token generation
2. ✅ **User Login** - Fully implemented with token retrieval
3. ✅ **Token Authentication** - Properly configured and working
4. ✅ **Views and Serializers** - All necessary components implemented
5. ✅ **Error Handling** - Proper validation and error responses
6. ✅ **Security** - Passwords hashed, tokens secure

The accounts app is now fully functional and meets all the requirements for user registration, login, and token retrieval!
