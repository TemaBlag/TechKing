from django.urls import include, path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls')),
    path('social-login/', views.UserLoginView.as_view(), name='social_login'),
]