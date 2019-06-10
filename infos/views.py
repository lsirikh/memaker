from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
#from django.views.generic import ListView
from infos.models import ServiceUsage, PrivacyPolicy

# Create your views here.
import logging
logger = logging.getLogger(__name__)

#--DetailView
class PrivacyPolicyView(TemplateView):
    template_name = 'infos/privacy_policy.html'

    def get_context_data(self, **kwargs):   #get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        context['content'] = PrivacyPolicy.objects.get(pk=self.kwargs.get('pk'))

        return context


#--DetailView
class ServiceUsagePolicyView(TemplateView):
    template_name = 'infos/service_policy.html'

    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        context['content'] = ServiceUsage.objects.get(pk=self.kwargs.get('pk'))

        return context