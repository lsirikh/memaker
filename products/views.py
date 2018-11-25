from django.shortcuts import render
from .models import Category, Product, Detail
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
#-- Codes for logging
import logging
logger = logging.getLogger(__name__)

#class ProductModelView(TemplateView):
#    template_name = 'products/index.html'
#
#    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
#        context = super().get_context_data(**kwargs)
#        context['model_list'] = [Category.objects.all(),
#                                 Product.objects.all(),
#                                 Detail.objects.all(), ]
#        return context

class ProductListView(ListView):
    template_name = 'products/index.html'
    model = Product
    paginate_by = 6
    context_object_name = 'product_list'
    queryset = Product.objects.all().order_by('-id')

class BookListView(ListView):
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'
    paginate_by = 6
    queryset = Product.objects.filter(category__title='교재')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = '교재'
        return context


class KitListView(ListView):
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'
    paginate_by = 6
    queryset = Product.objects.filter(category__title='조립키트')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = '조립키트'
        return context


class BoardListView(ListView):
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'
    paginate_by = 6
    queryset = Product.objects.filter(category__title='코딩보드')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = '코딩보드'
        return context

class UnplugedListView(ListView):
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'
    paginate_by = 6
    queryset = Product.objects.filter(category__title='언플러그드')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = '언플러그드'
        return context




class ProductDetailView(DetailView):
    model = Product
