from django.views.generic import TemplateView, DetailView
from models import Class, File, Evaluation, Subject, Teacher


class NavPanelMixin(object):
    def get_context_data(self, **kwargs):
        context = super(NavPanelMixin, self).get_context_data()
        context['list_class'] = Class.objects.all()
        return context

class NavBarMixin(object):
    def get_context_data(self, **kwargs):
        context = super(NavBarMixin, self).get_context_data()
        context['subjects'] = Subject.objects.all()
        context['teachers'] = Teacher.objects.all()
        return context


class ClassDetail(NavBarMixin, NavPanelMixin, DetailView):
    model = Class
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(ClassDetail, self).get_context_data()
        # context['files'] = File.objects.filter(evaluation_id=self.object)
        context['files'] = File.objects.filter(evaluation_id__class_id=self.object.class_id)
        context['evaluations'] = Evaluation.objects.filter(class_id=self.object.class_id)
        return context


class Home(NavBarMixin, NavPanelMixin, TemplateView):
    template_name = 'home.html'