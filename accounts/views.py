from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


# Create your views here.
from .models import *
#from .forms import CreateUserForm
from .forms import SignUpForm

def index_view(request):
    return render(request, 'index.html')


#@login_required
#def dashboard_view(request):
    #return render(request, '/results/templates/dashboard.html')

def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            #group = Group.objects.get(name=form.position)
            user.groups.add(form.cleaned_data['position'])
            return redirect('login_url')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

