from django.shortcuts import render
from .models import Category, Product, Detail
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from accounts.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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

@login_required(login_url="accounts:login")
def favorite_add_view(request, pk):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    userprofile = UserProfile.objects.get(user__username=request.user)
    requested_product = Product.objects.get(pk=pk)
    # 관심 상품 등록 과정
    userprofile.favorite_product.add(requested_product)

    for lecture in userprofile.favorite_product.all():
        if lecture.pk == pk:
            args = {
                'object': requested_product,
                'user_profile': userprofile,
                'isRegistered': True
            }
            break;
        else:
            # 여기는 당연히 나올 수 없는 코드
            print("이 코드가 실행되면 오류!")
            args = {
                'object': requested_product,
                'user_profile': userprofile,
                'isRegistered': False
            }
    # next = request.GET.get('next', '/')  # next 기능은 작동 안됨
    return_url = 'products/product_detail.html'
    print(return_url)
    print(args)
    return render(request, return_url, args)


@login_required(login_url="accounts:login")
def favorite_sub_view(request, pk):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    user = auth.get_user(request)
    userprofile = UserProfile.objects.get(user__username=request.user)
    requested_product = Product.objects.get(pk=pk)
    # 관심강좌 등록 해제.....
    userprofile.favorite_product.remove(requested_product)

    try:

        for lecture in userprofile.favorite_product.all():
            if lecture.pk == pk:
                # 여기는 당연히 나올 수 없는 코드 관심 강좌 등록을 해제했으니까....
                print("이 코드가 실행되면 오류!")
                args = {
                    'object': requested_product,
                    'user_profile': userprofile,
                    'isRegistered': True
                }
                print(args)
                break;
            else:
                args = {
                    'object': requested_product,
                    'user_profile': userprofile,
                    'isRegistered': False
                }
        print(args)
    except:
        args = {
            'object': requested_product,
            'user_profile': userprofile,
            'isRegistered': False
        }
        print(args)


    # next = request.GET.get('next', '/')  # next 기능은 작동 안됨
    return_url = 'accounts/dash_board.html'
    print(return_url)

    return render(request, return_url, args)







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
    ##페이지 네이션 기능을 동작시키기 위해서는 queryset을 사용하고,
    ## get_context_data()를 활용해서 dict에 category로 교재를 넣어준다.
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
