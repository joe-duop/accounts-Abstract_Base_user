# accounts-Abstract_Base_user
overrides the default auth models that comes with django and replaced with a customized user model

first commit
project created abstractbase, App created called accounts and registered in the settings.py under the installed apps.
updated the templates section in the settings.py    --the DIRS section.


second commit
created a customuser model with two classes to overide the default user model and replace username with an email.
userprofile class
created a userprofile class with parameters abstractbaseuser and permissionmixins.
this overides the current user model and i created my own new customuser models.
userprofilemanager class
created a userprofilemanager class with parameter BaseUserManager to manage the creation of normalusers and superusers.
i registered the custom model in the settings.py and then ran migrations.


third commit
registed my customuser model in the admin.py  to access it in the localhost:8000/admin.
created a superuser with an email and a password. and logged in the localhost:8000/admin.


forth commit
created a signup-url-view-template
then created a forms.py and inside i created a class
created a class CustomUserCreationForm with parameter UserCreationForm
this is to change the default signup form to match my customuser models and also accept email instead of a username and othe fields.


fifth commit
in the admin.py i created a class called CustomUserAdmin with parameter UserAdmin
this is to rectify the messy user details in the localhost:8000/admin template.
this is to arrange the user-details in default mode since i overrided the default one.
i then registed the CustomUserAdmin model in the admin.py together with the customuser.


sixth commit
defined a signup-view that saves registed user.
i used the default login funtion to login users by including django.contrib.auth.urls in the base urls.
i created the login.html in the apps template/registration directory to inherit the default login funtionality.
i updated the settings.py to redirect logged-in and signed-up users to home.html






