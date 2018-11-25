# Create your views here.
from django.views.generic.base import TemplateView
#from django.views.generic import ListView
from .models import Intro
#from memaker.lectures.models import Lecture

#-- Codes for logging
import logging
logger = logging.getLogger(__name__)

#--TemplateView
class IntroIndexView(TemplateView):
    template_name = 'intro/index.html'

    def get_context_data(self, **kwargs):   #get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        context['model_list'] = Intro.objects.all()

        return context
