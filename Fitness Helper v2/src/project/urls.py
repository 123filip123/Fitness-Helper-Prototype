"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('workouts/',workouts_view,name='workouts'),
    path('workouts',workouts_view,name='workouts'),
    path('workouts/<str:name>',split_view,name='split'),
    path('exercises',exercises_view,name='exercises'),
    path('exercises/<str:name>',muscle_view,name='muscle'),
    path('quiz',quiz_view,name='quiz'),
    path('quiz-results',quizResults_view,name='quiz-results'),
    path('login',login_view,name='login'),
    path('register',register_view,name='register'),
    path('logout',logout_view,name='logout'),
    path('certificate',certificate_view,name='certificate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
