from django.views.generic.base import TemplateView
from products.models import Content
#from lectures.models import Lecture


#-- TemplateView

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        print("HomeView Start")
        context = super().get_context_data(**kwargs)
        context = {'product_list':Content.objects.filter(category__section='상품', isShow = True, recommend__in=[1, 2])[:3],
                   'lecture_list':Content.objects.filter(category__section='강좌', isShow = True, recommend__in=[1, 2])[:3]}
        return context

#def login_redirect(request):
#    return redirect('accounts:login')

class IconView(TemplateView):
    template_name = 'google2cea96b33d0c202f.html'

class GoogleView(TemplateView):
    template_name = 'google2cea96b33d0c202f.html'

class GoogleView2nd(TemplateView):
    template_name = 'google640e077116d2555d.html'

class NaverView(TemplateView):
    template_name = 'navere8566efa5b506b61efd740303a95e363.html'

class NaverRobot(TemplateView):
    template_name = 'robots.txt'
