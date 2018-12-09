from django.shortcuts import render
from .models import Section, Category, Lecture, Video
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from accounts.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from memaker.products.models import Product as products_Product
# Create your views here.
# -- Codes for logging
import logging

logger = logging.getLogger(__name__)


# class LectureModelView(TemplateView):
#    template_name = 'lectures/index.html'
#
#    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
#        context = super().get_context_data(**kwargs)
#        context['model_list'] = [Category.objects.all(),
#                                 Section.objects.all(),
#                                 Lecture.objects.all(), ]
#        return context

@login_required(login_url="accounts:login")
def favorite_add_view(request, pk):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    userprofile = UserProfile.objects.get(user__username=request.user)
    requested_lecture = Lecture.objects.get(pk=pk)
    # 관심 강의 등록 과정
    userprofile.favorite_lecture.add(requested_lecture)

    for lecture in userprofile.favorite_lecture.all():
        if lecture.pk == pk:
            args = {
                'object': requested_lecture,
                'user_profile': userprofile,
                'isRegistered': True
            }
            break;
        else:
            # 여기는 당연히 나올 수 없는 코드
            print("이 코드가 실행되면 오류!")
            args = {
                'object': requested_lecture,
                'user_profile': userprofile,
                'isRegistered': False
            }
    # next = request.GET.get('next', '/')  # next 기능은 작동 안됨
    return_url = 'lectures/lecture_detail.html'
    print(return_url)
    print(args)
    return render(request, return_url, args)


@login_required(login_url="accounts:login")
def favorite_sub_view(request, pk):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    user = auth.get_user(request)
    userprofile = UserProfile.objects.get(user__username=request.user)
    requested_lecture = Lecture.objects.get(pk=pk)
    # 관심강좌 등록 해제.....
    userprofile.favorite_lecture.remove(requested_lecture)

    try:

        for lecture in userprofile.favorite_lecture.all():
            if lecture.pk == pk:
                # 여기는 당연히 나올 수 없는 코드 관심 강좌 등록을 해제했으니까....
                print("이 코드가 실행되면 오류!")
                args = {
                    'object': requested_lecture,
                    'user_profile': userprofile,
                    'isRegistered': True
                }
                print(args)
                break;
            else:
                args = {
                    'object': requested_lecture,
                    'user_profile': userprofile,
                    'isRegistered': False
                }
        print(args)
    except:
        args = {
            'object': requested_lecture,
            'user_profile': userprofile,
            'isRegistered': False
        }
        print(args)


    # next = request.GET.get('next', '/')  # next 기능은 작동 안됨
    return_url = 'accounts/dash_board.html'
    print(return_url)

    return render(request, return_url, args)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user = auth.get_user(self.request)
            number = self.kwargs.get(self.pk_url_kwarg)
            userprofile = UserProfile.objects.get(user__username=user)
            context['userprofile'] = userprofile
            print(number)
            for lecture in userprofile.favorite_lecture.all():
                if lecture.pk == number:
                    print("같은 강의가 있음 : " + lecture.title)
                    context['isRegistered'] = True
                    break;
                else:
                    context['isRegistered'] = False
                    print("같은 강의가 없음 ")

        except:
            pass

        return context
