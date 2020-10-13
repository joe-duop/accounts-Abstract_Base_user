from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import CustomUserCreationForm

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
                form.save()
                return redirect('home')
        return render(request, 'signupuser.html', {'form':form})

    

