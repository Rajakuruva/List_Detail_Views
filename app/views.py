from django.shortcuts import render
from django.views.generic import *
from app.models import *
# Create your views here.
class home(TemplateView):
    template_name='app/Home.html'

class School_list(ListView):
    model=School
    context_object_name='schools'

class School_detail(DetailView):
    model=School
    context_object_name='sclobj'

class Schoolcreate(CreateView):
    model=School
    fields="__all__"

