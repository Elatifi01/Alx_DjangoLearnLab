from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from posts.models import Post
from posts.serializers import PostSerializer
from django.http import JsonResponse


def accounts_root(request):
    """Root accounts endpoint that lists all available account endpoints"""
    return JsonResponse({
        'message': 'Accounts API',
        'endpoints': {
            'register': '/api/accounts/register/',
            'login': '/api/accounts/login/',
            'profile': '/api/accounts/profile/',
            'follow_user': '/api/accounts/follow/<user_id>/',
            'unfollow_user': '/api/accounts/unfollow/<user_id>/',
        }
    })


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []  # Allow unauthenticated access for registration
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests to show register endpoint information"""
        return Response({
            'message': 'User Registration endpoint',
            'method': 'POST',
            'required_fields': {
                'username': 'string (required)',
                'password': 'string (required)',
                'email': 'string (required)',
                'bio': 'string (optional)'
            },
            'example_request': {
                'username': 'john_doe',
                'password': 'secure_password123',
                'email': 'john@example.com',
                'bio': 'Hello, I am John!'
            },
            'success_response': {
                'id': 'user_id',
                'username': 'john_doe',
                'email': 'john@example.com',
                'bio': 'Hello, I am John!',
                'token': 'auto_generated_auth_token'
            },
            'notes': [
                'Password will be securely hashed',
                'Authentication token is automatically created',
                'Bio field is optional'
            ]
        })
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'bio': user.bio,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

class LoginView(ObtainAuthToken):
    permission_classes = []  # Allow unauthenticated access for login
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests to show login endpoint information"""
        return Response({
            'message': 'Login endpoint',
            'method': 'POST',
            'required_fields': {
                'username': 'string',
                'password': 'string'
            },
            'example_request': {
                'username': 'your_username',
                'password': 'your_password'
            },
            'success_response': {
                'token': 'your_auth_token',
                'user_id': 'user_id',
                'email': 'user_email'
            }
        })
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = CustomUser.objects.get(id=token.user_id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def get(self, request, *args, **kwargs):
        """Override to provide helpful information or user profile"""
        if request.user.is_authenticated:
            # Return the actual user profile
            return super().get(request, *args, **kwargs)
        else:
            # Return helpful information for unauthenticated users
            return Response({
                'message': 'User Profile endpoint',
                'methods': ['GET', 'PUT', 'PATCH'],
                'authentication': 'Required - you must be logged in',
                'description': {
                    'GET': 'Retrieve your profile information',
                    'PUT': 'Update your entire profile',
                    'PATCH': 'Partially update your profile'
                },
                'available_fields': {
                    'username': 'string',
                    'email': 'string',
                    'bio': 'string',
                    'profile_picture': 'string (URL)',
                    'followers': 'array (read-only)'
                }
            }, status=401)


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        """Handle GET requests to show follow endpoint information"""
        try:
            user_to_follow = get_object_or_404(CustomUser, id=user_id)
            is_following = request.user.following.filter(id=user_id).exists()
            
            return Response({
                'message': 'Follow user endpoint',
                'method': 'POST',
                'target_user': {
                    'id': user_to_follow.id,
                    'username': user_to_follow.username
                },
                'current_status': 'following' if is_following else 'not following',
                'action': 'Use POST to follow this user' if not is_following else 'Already following - use unfollow endpoint',
                'authentication': 'Required - you must be logged in'
            })
        except:
            return Response({
                'message': 'Follow user endpoint',
                'method': 'POST',
                'user_id': user_id,
                'error': 'User not found',
                'authentication': 'Required - you must be logged in'
            })

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        """Handle GET requests to show unfollow endpoint information"""
        try:
            user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
            is_following = request.user.following.filter(id=user_id).exists()
            
            return Response({
                'message': 'Unfollow user endpoint',
                'method': 'POST',
                'target_user': {
                    'id': user_to_unfollow.id,
                    'username': user_to_unfollow.username
                },
                'current_status': 'following' if is_following else 'not following',
                'action': 'Use POST to unfollow this user' if is_following else 'Not following - use follow endpoint',
                'authentication': 'Required - you must be logged in'
            })
        except:
            return Response({
                'message': 'Unfollow user endpoint',
                'method': 'POST',
                'user_id': user_id,
                'error': 'User not found',
                'authentication': 'Required - you must be logged in'
            })

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)


class UserFeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
