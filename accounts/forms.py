from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile



class CustomUserCreationForm(UserCreationForm):
    """overriding the usercreationform template to match with my customuser model - userprofile"""
    class Meta:
        model = UserProfile
        fields = ['email', 'name']



