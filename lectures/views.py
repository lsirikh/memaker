from django.shortcuts import render
from .models import Section, Category, Lecture, Video
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
#from memaker.products.models import Product as products_Product
# Create your views here.
#-- Codes for logging
import logging
logger = logging.getLogger(__name__)


#class LectureModelView(TemplateView):
#    template_name = 'lectures/index.html'
#
#    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
#        context = super().get_context_data(**kwargs)
#        context['model_list'] = [Category.objects.all(),
#                                 Section.objects.all(),
#                                 Lecture.objects.all(), ]
#        return context

class LectureListView(ListView):
    template_name = 'lectures/index.html'
    model = Lecture
    paginate_by = 6
    context_object_name = 'lecture_list'
    queryset = Lecture.objects.all().order_by('-updated')

class EntryListView(ListView):
    template_name = 'lectures/lecture_list.html'
    context_object_name = 'lecture_list'
    model = Lecture
    paginate_by = 6
    queryset = Lecture.objects.filter(category__title='엔트리')

class MakerListView(ListView):
    template_name = 'lectures/lecture_list.html'
    context_object_name = 'lecture_list'
    model = Lecture
    paginate_by = 6
    queryset = Lecture.objects.filter(category__title='메이커')

class ScratchListView(ListView):
    template_name = 'lectures/lecture_list.html'
    context_object_name = 'lecture_list'
    model = Lecture
    paginate_by = 6
    queryset = Lecture.objects.filter(category__title='스크래치')


class LectureDetailView(DetailView):
    model = Lecture
