from django.shortcuts import render
from django.views.generic import TemplateView
from models import Teacher, Class, Subject

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['message']='Welcome to RapidClass 0.1'
        context['teachers'] = Teacher.objects.all()
        context['subjects'] = Subject.objects.all()
        context['classes'] = Class.objects.all()
        return context
