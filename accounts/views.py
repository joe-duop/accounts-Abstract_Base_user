from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import CustomUserCreationForm

# Create your views here.
def signupuser(request):
    return render(request, 'signupuser.html', {'form':CustomUserCreationForm()})

