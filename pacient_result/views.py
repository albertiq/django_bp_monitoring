from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Pacient_table, Recomend_table
from django.contrib.auth.decorators import login_required
#from accounts.forms import CreateUserForm
from django.contrib.auth import models
from django.contrib.auth.models import User, Group
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse



@login_required
def index(request):
    if request.user.groups.filter(name='Пациент').exists():
        datas = Pacient_table.objects.filter(username=request.user)
        return render(request, "dashboard.html", {"datas": datas})
    else:
        group = models.Group.objects.get(name='Пациент')
        users = group.user_set.all()
        data_pac =  Pacient_table.objects.values('username', 'user_id_id').distinct()
        #data_pac =  Pacient_table.objects.all()
        num_users = group.user_set.all().count()
        recomendations = Recomend_table.objects.all().count()
        return render(request, "dashboard_doctor.html", {"users": users, "data_pac": data_pac, 'num_users': num_users, 'recomendations': recomendations})

class PacientList(generic.ListView):
    model = Pacient_table
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(PacientList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['pac'] = Pacient_table.objects.values('username', 'user_id_id').distinct()
        context['user_list'] = User.objects.values('username', 'id', 'first_name', 'last_name')
        return context


class PacientDetail(DetailView):
    model = User
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['res_list'] = Pacient_table.objects.all()
        context['user_list'] = User.objects.values('username', 'id', 'first_name', 'last_name')
        return context


class Recomend_create(CreateView):
    model = Recomend_table
    fields = '__all__'
    #initial={'pacient':'12/10/2016',}
    def get_success_url(self):
            return reverse('pacients')

class RecomendList(generic.ListView):
    model = Recomend_table
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(RecomendList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['rec_list'] = Recomend_table.objects.all()
        context['user_list'] = User.objects.all()

        return context

class RecomendList_pacient(generic.ListView):
    model = Recomend_table
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(RecomendList_pacient, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['rec_list'] = Recomend_table.objects.all()
        return context