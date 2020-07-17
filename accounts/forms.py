from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.urls import reverse


class SignUpForm(UserCreationForm):
    #position = forms.ChoiceField(choices=GROUP,  required=False)
    position = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    middle_name = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username', 'email',  'first_name', 'last_name', 'middle_name', 'password1', 'password2', 'position']

'''
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User

		fields = ['username', 'email', 'password1', 'password2', 'position']
'''
