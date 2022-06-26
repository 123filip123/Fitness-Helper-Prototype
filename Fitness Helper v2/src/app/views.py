from cmath import e
from datetime import date
from django.shortcuts import get_object_or_404, render, redirect
from app.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from app.models import Exercise, Muscle, Split, Workout, Profile

# Create your views here.


def home_view(request):
    return render(request,'home.html')

def workouts_view(request):
    return render(request,'workouts.html')

def split_view(request,name):
    workout = get_object_or_404(Workout,name=name)
    splits = Split.objects.filter(workout=workout)
    return render(request,'split.html',{'splits':splits,'workout':workout})

def exercises_view(request):
    muscles = Muscle.objects.all()
    return render(request,'exercises.html',{'muscles':muscles})

def muscle_view(request,name):
    muscle = get_object_or_404(Muscle,name=name)
    return render(request,'muscle.html',{'muscle':muscle})


def quiz_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = UserForm(request.POST)
        correct = 0
        if form.is_valid:
            q1 = request.POST['q1']
            q2 = request.POST['q2']

            if q1 == '2':
                correct+=1
            if q2 == '1':
                correct+=1

            got_certified = False
            user = get_object_or_404(User,username=request.user.username)
            profile = get_object_or_404(Profile,user=user)
            if profile.highScore < int(correct):
                profile.highScore = int(correct)
            if int(correct) == 2 and not profile.certified:
                profile.certified = True
                profile.dateAcquired = date.today()
                got_certified = True

            user.save()
            profile.save()

            return render(request,'quiz-results.html',{'correct':correct,'got_certified':got_certified})

    else:
        form = UserForm()
    return render(request,'quiz.html',{'form':form})

def quizResults_view(request,correct,got_certified):
    got_certified = 0
    user = get_object_or_404(username=request.user.username)
    profile = get_object_or_404(user=user)
    if profile.highScore < int(correct):
        profile.highScore = int(correct)
    if int(correct) == 2 and not user.certified:
        user.certified = True
        got_certified = 1

    user.save()
    profile.save()

    return render(request,'quiz-results.html',{'correct':correct,'got_certified':got_certified})


def login_view(request):
    if request.method == "POST":
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page. 
        else:
            # Return an 'invalid login' error message.
            messages.success(request,("Error logging in... Try again..."))
            return redirect('login')
    else:
        return render(request,'login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['inputUsername']
        password = request.POST['inputPassword']
        password1 = request.POST['inputPassword2']
        email = request.POST['inputEmail']
        if username and password and email and password1:

            if password != password1:
                messages.success(request,("Passwords don't match... Try again..."))
                return redirect('register')

            try:
                go = User.objects.get(username=username)
                messages.success(request,("Username already exists... Try again..."))
                return redirect('register')
            except User.DoesNotExist:
                try:
                    go = User.objects.get(email=email)
                    messages.success(request,("Email already exists... Try again..."))
                    return redirect('register')
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    profile = Profile(user=user)
                    profile.save()
                    login(request, user)
                    return redirect('home')
        else:
            messages.success(request,("Something went wrong... Try again..."))
            return redirect('register')

    else:
        return render(request,'register.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def certificate_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    

    return render(request,'certificate.html')