from django.urls import path
from . import views
from .views import PasswordsChangeView, UserEditView
from django.contrib.auth import views as auth_views

app_name = 'home'
urlpatterns = [
    path('home/', views.get_index, name = 'home'),
    path('view-profile/', views.view_profile, name = 'view_profile'),
    path('register/', views.registerUser.as_view(), name = 'registerUser'),
    path('login/', views.loginUser.as_view(), name = 'loginUser'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),

    path('profile/edit/', UserEditView.as_view(), name = 'edit_profile'),
    path('profile/password/', PasswordsChangeView.as_view(template_name='home/change_password.html')),
]