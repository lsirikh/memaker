# from django.shortcuts import render, redirect
# from .models import Section, Category, Lecture, Video
# from django.views.generic.base import TemplateView
# from django.views.generic import ListView
# from django.views.generic import DetailView
# from accounts.models import UserProfile
# from django.contrib import auth
# from django.contrib.auth.decorators import login_required
# # from memaker.products.models import Product as products_Product
# # Create your views here.
# # -- Codes for logging
# import logging
#
# logger = logging.getLogger(__name__)
#
#
# # class LectureModelView(TemplateView):
# #    template_name = 'lectures/index.html'
# #
# #    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
# #        context = super().get_context_data(**kwargs)
# #        context['model_list'] = [Category.objects.all(),
# #                                 Section.objects.all(),
# #                                 Lecture.objects.all(), ]
# #        return context
#
# @login_required(login_url="accounts:login")
# def favorite_add_view(request, pk):
#     # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
#     userprofile = UserProfile.objects.get(user__username=request.user)
#     requested_lecture = Lecture.objects.get(pk=pk)
#     # 관심 강의 등록 과정
#     try:
#         userprofile.favorite_lecture.add(requested_lecture)
#     except:
#         print("관심상품 등록는 중에 오류가 발생했습니다.")
#
#     return redirect('lectures:lecture_detail', pk=pk)
#
#
# @login_required(login_url="accounts:login")
# def favorite_sub_view(request, pk):
#     # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
#     user = auth.get_user(request)
#     userprofile = UserProfile.objects.get(user__username=request.user)
#     requested_lecture = Lecture.objects.get(pk=pk)
#
#     try:
#         # 관심강좌 등록 해제.....
#         userprofile.favorite_lecture.remove(requested_lecture)
#
#     except:
#         print("관심강좌 해제하는 중에 오류가 발생했습니다.")
#         pass
#
#     return redirect('accounts:index')
#
#
# class LectureListView(ListView):
#     template_name = 'lectures/index.html'
#     model = Lecture
#     paginate_by = 6
#     context_object_name = 'lecture_list'
#     queryset = Lecture.objects.all().order_by('-updated')
#
#
# class EntryListView(ListView):
#     template_name = 'lectures/lecture_list.html'
#     context_object_name = 'lecture_list'
#     model = Lecture
#     paginate_by = 6
#     queryset = Lecture.objects.filter(category__title='엔트리')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.get(title='엔트리')
#         return context
#
#
# class MakerListView(ListView):
#     template_name = 'lectures/lecture_list.html'
#     context_object_name = 'lecture_list'
#     model = Lecture
#     paginate_by = 6
#     queryset = Lecture.objects.filter(category__title='메이커')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category = Category.objects.get(title='메이커')
#         context['category'] = category
#         print(category)
#         return context
#
# class ScratchListView(ListView):
#     template_name = 'lectures/lecture_list.html'
#     context_object_name = 'lecture_list'
#     model = Lecture
#     paginate_by = 6
#     queryset = Lecture.objects.filter(category__title='스크래치')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.get(title='스크래치')
#
#         return context
#
# class LectureDetailView(DetailView):
#     model = Lecture
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         lecture = Lecture.objects.get(pk=self.kwargs.get('pk'))
#
#         try:
#             selected_user = lecture.userprofile_set.get(user=self.request.user)
#             if (selected_user is not None):
#                 context['isRegistered'] = True
#                 print(selected_user)
#                 print("등록된 사용자")
#
#         except:
#             print("등록안된 사용자")
#             context['isRegistered'] = False
#
#         return context
