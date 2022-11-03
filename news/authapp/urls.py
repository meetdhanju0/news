from django.urls import path
from .views import *


urlpatterns = [
    path('', LoginView.as_view(), name='login'),


    path('forgot-password', ForgotPass.as_view(), name='forgot_password'),

    path('change-password/<int:code>', EditPassword.as_view(), name='change_password'),

    path('logout', LogoutView.as_view(), name='logout'),


    path('signup', SignUpView.as_view(), name='signup'),
   
]
