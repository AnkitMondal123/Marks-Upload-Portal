from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'name', 'phone_number', 'is_approved', 'is_admin',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'name', 'phone_number', 'is_approved', 'is_admin',)



class MyCustomSignupForm(SignupForm):
    
    name = forms.CharField(max_length=100, label='Full Name')
    phone_number = forms.CharField(max_length=15, label='Phone Number')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user