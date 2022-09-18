from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<pk>/profile/', ProfileDetailView.as_view(), name='profile'),
    path('<pk>/profile-img/', ProfileImageView.as_view(), name='profile_image'),
    path('<pk>/profile-img/<pic_name>/', ProfileImageUpdateView.as_view(), name='profile_image_confirm'),
    path('password-change/', PasswordChangeCustomView.as_view(), name='password_change'),
]
