from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('activate/<email_token>/', activate_email, name='activate'),
]
