from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'signupuser.html', {'form':CustomUserCreationForm()})
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('current')
        return render(request, 'signupuser.html', {'form':form})


def current(request):
    return render(request, 'current.html')

    

