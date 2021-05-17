from django.contrib.auth import views
from django.urls import path

from .views import SignUpView

from accounts import views

urlpatterns = [
    
    path('auth/', SignUpView.as_view()),
]
