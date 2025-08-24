# Social Media API - Django REST Framework

*Week of August 18-24, 2025*

## 📋 Project Overview

A comprehensive social media API built with Django REST Framework, featuring user authentication, posts management, social interactions, and real-time notifications. This project was developed during the week of August 18-24, 2025, as part of the ALX Django Learning Lab curriculum.

## 🚀 Features Implemented This Week

### 🔐 User Authentication & Management
- **Custom User Model** with extended fields (bio, profile picture, followers)
- **Token-based Authentication** using Django REST Framework
- **User Registration** with automatic token generation
- **User Login** with token retrieval
- **Profile Management** for authenticated users
- **Follow/Unfollow System** for user interactions

### 📝 Posts & Content Management
- **Post Creation** with content and timestamps
- **Post Retrieval** with proper pagination
- **Like System** for post interactions
- **User Feed** showing posts from followed users
- **Author Attribution** linking posts to users

### 🔔 Notifications System
- **Notification Model** for user alerts
- **API Endpoints** for notification management
- **User-specific Notifications** with proper filtering

### 🌐 API Architecture
- **RESTful Design** following best practices
- **Proper HTTP Status Codes** for all responses
- **JSON Serialization** for all data exchanges
- **Error Handling** with descriptive messages
- **Documentation Endpoints** for API exploration

## 🏗️ Project Structure

```
social_media_api/
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database
├── check_users.py                     # User verification utility
├── test_accounts_api.py               # API testing script
├── ACCOUNTS_IMPLEMENTATION.md         # Implementation documentation
├── README.md                          # This file
├── accounts/                          # User management app
│   ├── models.py                      # CustomUser model
│   ├── serializers.py                # User serializers
│   ├── views.py                       # Authentication views
│   ├── urls.py                        # Account endpoints
│   ├── admin.py                       # Admin configuration
│   ├── management/commands/           # Custom management commands
│   └── migrations/                    # Database migrations
├── posts/                             # Posts management app
│   ├── models.py                      # Post and Like models
│   ├── serializers.py                # Post serializers
│   ├── views.py                       # Post views
│   ├── urls.py                        # Post endpoints
│   └── migrations/                    # Database migrations
├── notifications/                     # Notifications app
│   ├── models.py                      # Notification model
│   ├── serializers.py                # Notification serializers
│   ├── views.py                       # Notification views
│   ├── urls.py                        # Notification endpoints
│   └── migrations/                    # Database migrations
└── social_media_api/                  # Main project configuration
    ├── settings.py                    # Django settings
    ├── urls.py                        # Main URL configuration
    ├── wsgi.py                        # WSGI configuration
    └── asgi.py                        # ASGI configuration
```

## 🔧 Technology Stack

- **Backend Framework**: Django 5.2.4
- **API Framework**: Django REST Framework
- **Database**: SQLite (development)
- **Authentication**: Token-based authentication
- **Python Version**: 3.12/3.13
- **Development Environment**: VS Code

## 📦 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- pip package manager
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd social_media_api
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   pip install Pillow  # For image handling
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 🛠️ API Endpoints

### Authentication Endpoints
| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/api/accounts/register/` | User registration | None |
| POST | `/api/accounts/login/` | User login | None |
| GET/PUT/PATCH | `/api/accounts/profile/` | User profile management | Token required |
| POST | `/api/accounts/follow/<user_id>/` | Follow a user | Token required |
| POST | `/api/accounts/unfollow/<user_id>/` | Unfollow a user | Token required |

### Posts Endpoints
| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET/POST | `/api/posts/` | List/Create posts | Token required |
| GET/PUT/DELETE | `/api/posts/<id>/` | Post detail/update/delete | Token required |
| POST | `/api/posts/<id>/like/` | Like/Unlike a post | Token required |
| GET | `/api/posts/feed/` | User's personalized feed | Token required |

### Notifications Endpoints
| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/notifications/` | List user notifications | Token required |
| PATCH | `/api/notifications/<id>/read/` | Mark notification as read | Token required |

## 📝 Usage Examples

### User Registration
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123",
    "email": "john@example.com",
    "bio": "Hello, I am John!"
  }'
```

**Response:**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "bio": "Hello, I am John!",
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### User Login
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

**Response:**
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "user_id": 1,
  "email": "john@example.com"
}
```

### Create a Post
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "This is my first post!"
  }'
```

### Get User Profile
```bash
curl -X GET http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

## 🧪 Testing

### Automated Testing
Run the API test suite:
```bash
python test_accounts_api.py
```

### Manual Testing
Use tools like:
- **Postman** for comprehensive API testing
- **curl** for command-line testing
- **Django Admin** at `/admin/` for data management
- **Browser** for GET endpoints

### Test User Creation
```bash
python manage.py shell
```
```python
from accounts.models import CustomUser
user = CustomUser.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)
```

## 🔒 Security Features

- **Password Hashing** using Django's built-in security
- **Token Authentication** for API access
- **CSRF Protection** for web forms
- **Input Validation** through serializers
- **Permission Classes** for endpoint protection
- **User Isolation** - users can only access their own data

## 📊 Database Models

### CustomUser Model
- Extends Django's AbstractUser
- Additional fields: `bio`, `profile_picture`, `followers`
- Many-to-many relationship for following system

### Post Model
- Fields: `author`, `content`, `created_at`, `updated_at`
- Foreign key relationship to CustomUser

### Like Model
- Fields: `user`, `post`, `created_at`
- Unique constraint on user-post combination

### Notification Model
- Fields: `recipient`, `actor`, `verb`, `target`, `timestamp`, `read`
- Generic foreign key for flexible targeting

## 🚀 Development Highlights (This Week)

### Monday - Tuesday (Aug 18-19)
- Set up Django project structure
- Implemented CustomUser model
- Created basic authentication system

### Wednesday - Thursday (Aug 20-21)
- Developed Posts app with CRUD operations
- Implemented Like functionality
- Added user following system

### Friday - Saturday (Aug 22-23)
- Built Notifications system
- Enhanced API documentation
- Added comprehensive error handling

### Sunday (Aug 24)
- Finalized authentication flows
- Added API testing scripts
- Completed documentation

## 🔄 API Response Format

### Success Response
```json
{
  "data": {...},
  "status": "success",
  "message": "Operation completed successfully"
}
```

### Error Response
```json
{
  "error": "Error description",
  "status": "error",
  "details": {...}
}
```

## 🎯 Future Enhancements

- [ ] **Image Upload** for posts and profile pictures
- [ ] **Real-time Chat** using WebSockets
- [ ] **Push Notifications** for mobile apps
- [ ] **Advanced Search** with filters
- [ ] **Content Moderation** tools
- [ ] **Analytics Dashboard** for user engagement
- [ ] **Rate Limiting** for API endpoints
- [ ] **Caching** for improved performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is part of the ALX Django Learning Lab curriculum.

## 📞 Support

For questions or issues:
- Create an issue in the repository
- Contact the development team
- Refer to Django and DRF documentation

---

**Project Status**: ✅ Core functionality completed  
**Last Updated**: August 24, 2025  
**Version**: 1.0.0  
**Developer**: El Atifi Haitam (Alx student)
