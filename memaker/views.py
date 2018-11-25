from django.views.generic.base import TemplateView
from products.models import Product
from lectures.models import Lecture
from django.shortcuts import redirect


#-- TemplateView

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'product_list':Product.objects.all()[:3],
                   'lecture_list':Lecture.objects.all()[:3]}
        return context

#def login_redirect(request):
#    return redirect('accounts:login')