from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('home/', views.get_index, name = 'home'),
    path('view-profile/', views.view_profile, name = 'view_profile'),
    path('register/', views.registerUser.as_view(), name = 'registerUser'),
    path('login/', views.loginUser.as_view(), name = 'loginUser'),
    path('logout/', views.logoutUser, name = 'logout')
]