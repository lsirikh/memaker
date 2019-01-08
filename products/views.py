from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    render_to_response,
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from urllib.parse import urlencode
from products.models import (
    Category,
    Content,
    Product,
    Image,
    File,
    Lecture,
    Video,
    Product,
    Appraisal,
    ReplyChapter
)
from products.forms import (
    AppraisalForm,
    ReplyChapterForm
)
from django.views.generic.base import TemplateView
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from accounts.models import UserProfile
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
# -- Codes for logging
import logging

logger = logging.getLogger(__name__)


# class ProductModelView(TemplateView):
#    template_name = 'products/index.html'
#
#    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
#        context = super().get_context_data(**kwargs)
#        context['model_list'] = [Category.objects.all(),
#                                 Product.objects.all(),
#                                 Detail.objects.all(), ]
#        return context

@login_required(login_url="accounts:login")
def content_information_favorite_add_view(request, pk):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    userprofile = UserProfile.objects.get(user__username=request.user)
    requested_content = Content.objects.get(pk=pk)
    # 관심 상품 등록 과정
    try:
        userprofile.favorite.add(requested_content)
    except:
        print("관심상품 등록는 중에 오류가 발생했습니다.")

    return redirect('products:content_information', pk=pk)


# @login_required(login_url="accounts:login")
# def product_review_favorite_add_view(request, pk):
#     # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
#     userprofile = UserProfile.objects.get(user__username=request.user)
#     requested_content = Content.objects.get(pk=pk)
#     # 관심 상품 등록 과정
#     try:
#         userprofile.favorite.add(requested_content)
#     except:
#         print("관심상품 등록는 중에 오류가 발생했습니다.")
#
#     return redirect('products:content_product_review', pk=pk)

@login_required(login_url="accounts:login")
def content_information_favorite_sub_view(request, pk):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    userprofile = UserProfile.objects.get(user__username=request.user)
    requested_content = Content.objects.get(pk=pk)

    try:
        # 관심상품 등록 해제.....
        userprofile.favorite.remove(requested_content)
    except:
        print("관심상품 해제하는 중에 오류가 발생했습니다.")
        pass

    return redirect('accounts:index')


# @login_required(login_url="accounts:login")
# def product_reivew_favorite_sub_view(request, pk):
#     # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
#     userprofile = UserProfile.objects.get(user__username=request.user)
#     requested_content = Content.objects.get(pk=pk)
#
#     try:
#         # 관심상품 등록 해제.....
#         userprofile.favorite.remove(requested_content)
#     except:
#         print("관심상품 해제하는 중에 오류가 발생했습니다.")
#         pass
#
#     return redirect('accounts:index')
#
#
#
#
#
#
#
class ProductListView(ListView):
    template_name = 'products/index.html'
    model = Content
    paginate_by = 9
    context_object_name = 'content_list'

    def get_context_data(self, **kwargs):

        #########################################################
        # paginator의 오브젝트를 context 데이터에서 갖고 온다.
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        print(paginator)
        ##########################################################

        # pagenator의 페이지당 인덱스 수를 5로 설정한다.
        page_numbers_range = 5  # Display only 5 page numbers
        # set max_index as "int" from the length of paginator.page_range
        # print(type(paginator.page_range))
        # print(type(len(paginator.page_range)))
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        # python if syntax check!
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        # print("start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range")
        # print("{0} = int(({1} - 1) / {2}) * {3}".format(start_index, current_page, page_numbers_range,
        #                                                        page_numbers_range))
        end_index = start_index + page_numbers_range
        # print(end_index)

        #########next index checking and last index setting#######
        if end_index >= max_index:
            end_index = max_index
            has_next_index = False
        else:
            has_next_index = True

        ####################previous index checking###############
        if (start_index + 1) > 1:
            has_previous_index = True
        else:
            has_previous_index = False

        page_range = paginator.page_range[start_index:end_index]
        print("page_range type : " + str(type(page_range)))
        print("page_range : " + str(page_range))
        print("page_range len : " + str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index + 1) - page_numbers_range
        print((start_index + 1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        kwargs['section'] = '상품'
        kwargs['selected_base_page'] = 'base_products.html'
        ##########################################################

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        print("ProductListView is started")
        queryset = Content.objects.filter(category__section='상품')
        # print("queryset")
        # print(queryset)
        # print(queryset.first())
        # print(queryset.first().product)
        return queryset


class LectureListView(ListView):
    template_name = 'products/index.html'
    model = Content
    paginate_by = 9
    context_object_name = 'content_list'

    def get_context_data(self, **kwargs):
        ##########################################################
        # paginator의 오브젝트를 context 데이터에서 갖고 온다.
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        print(paginator)
        ##########################################################

        # pagenator의 페이지당 인덱스 수를 5로 설정한다.
        page_numbers_range = 5  # Display only 5 page numbers
        # set max_index as "int" from the length of paginator.page_range
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        # python if syntax check!
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        #########next index checking and last index setting#######
        if end_index >= max_index:
            end_index = max_index
            has_next_index = False
        else:
            has_next_index = True

        ####################previous index checking###############
        if (start_index + 1) > 1:
            has_previous_index = True
        else:
            has_previous_index = False

        page_range = paginator.page_range[start_index:end_index]
        print("page_range type : " + str(type(page_range)))
        print("page_range : " + str(page_range))
        print("page_range len : " + str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index + 1) - page_numbers_range
        print((start_index + 1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        kwargs['section'] = '강좌'
        kwargs['selected_base_page'] = 'base_lectures.html'
        ##########################################################
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        print("LectureListView is started")
        queryset = Content.objects.filter(category__section='강좌')
        return queryset


class ContentCategoryListView(ListView):
    template_name = 'products/content_list.html'
    model = Content
    paginate_by = 9
    context_object_name = 'content_list'

    def get_context_data(self, **kwargs):
        ##########################################################
        # paginator의 오브젝트를 context 데이터에서 갖고 온다.
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        print(paginator)
        ##########################################################

        # pagenator의 페이지당 인덱스 수를 5로 설정한다.
        page_numbers_range = 5  # Display only 5 page numbers
        # set max_index as "int" from the length of paginator.page_range
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        # python if syntax check!
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        #########next index checking and last index setting#######
        if end_index >= max_index:
            end_index = max_index
            has_next_index = False
        else:
            has_next_index = True

        ####################previous index checking###############
        if (start_index + 1) > 1:
            has_previous_index = True
        else:
            has_previous_index = False

        page_range = paginator.page_range[start_index:end_index]
        print("page_range type : " + str(type(page_range)))
        print("page_range : " + str(page_range))
        print("page_range len : " + str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index + 1) - page_numbers_range
        print((start_index + 1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        kwargs['category'] = self.category
        if self.category.section == '강좌':
            print("강좌선택")
            kwargs['selected_base_page'] = 'base_lectures.html'
        elif self.category.section == '상품':
            print("상품선택")
            kwargs['selected_base_page'] = 'base_products.html'
        ##########################################################

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        print("ContentCategoryListView is started")
        self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        print(self.category)
        queryset = Content.objects.filter(category=self.category)
        return queryset


#
# class KitListView(ListView):
#     context_object_name = 'product_list'
#     template_name = 'products/product_list.html'
#     paginate_by = 6
#     queryset = Product.objects.filter(category__title='조립키트')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.get(title='조립키트')
#         return context
#
#
# class BoardListView(ListView):
#     context_object_name = 'product_list'
#     template_name = 'products/product_list.html'
#     paginate_by = 6
#     queryset = Product.objects.filter(category__title='코딩보드')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.get(title='코딩보드')
#         return context
#
# class UnplugedListView(ListView):
#     context_object_name = 'product_list'
#     template_name = 'products/product_list.html'
#     paginate_by = 6
#     queryset = Product.objects.filter(category__title='언플러그드')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = Category.objects.get(title='언플러그드')
#         return context
#
#
#

# 강좌와 상품을 통합한 CBV 제작
class ContentInformationView(DetailView):
    model = Content
    template_name = 'products/content_information.html'

    def get_context_data(self, **kwargs):
        print("ContentInformationView is started")
        context = super().get_context_data(**kwargs)
        self.content = get_object_or_404(Content, pk=self.kwargs.get('pk'))
        content = self.content
        #content.file.first().file_extension()
        try:
            selected_user = content.userprofile_set.get(user=self.request.user)
            if (selected_user is not None):
                kwargs['isRegistered'] = True
                print(selected_user)
                print("등록된 사용자")

        except:
            print("등록안된 사용자")
            kwargs['isRegistered'] = False

        kwargs['content'] = self.content
        kwargs['content_list'] = Content.objects.all()
        if self.content.category.section == '강좌':
            print("강좌선택")
            kwargs['selected_base_page'] = 'base_lectures.html'
        elif self.content.category.section == '상품':
            print("상품선택")
            kwargs['selected_base_page'] = 'base_products.html'
        return super().get_context_data(**kwargs)


class ContentReviewView(ListView):
    template_name = 'products/content_review.html'
    model = Appraisal
    paginate_by = 5
    context_object_name = 'appraisal_list'

    def get_context_data(self, **kwargs):
        print("ContentReviewView is started")

        ##########################################################
        # paginator의 오브젝트를 context 데이터에서 갖고 온다.
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        print(paginator)
        ##########################################################

        # pagenator의 페이지당 인덱스 수를 5로 설정한다.
        page_numbers_range = 5  # Display only 5 page numbers
        # set max_index as "int" from the length of paginator.page_range
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        # python if syntax check!
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        #########next index checking and last index setting#######
        if end_index >= max_index:
            end_index = max_index
            has_next_index = False
        else:
            has_next_index = True

        ####################previous index checking###############
        if (start_index + 1) > 1:
            has_previous_index = True
        else:
            has_previous_index = False

        page_range = paginator.page_range[start_index:end_index]
        print("page_range type : " + str(type(page_range)))
        print("page_range : " + str(page_range))
        print("page_range len : " + str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index + 1) - page_numbers_range
        print((start_index + 1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        try:
            selected_user = self.content.userprofile_set.get(user=self.request.user)
            if (selected_user is not None):
                kwargs['isRegistered'] = True
                print(selected_user)
                print("등록된 사용자")

        except:
            print("등록안된 사용자")
            kwargs['isRegistered'] = False

        kwargs['content'] = self.content
        if self.content.category.section == '강좌':
            print("강좌선택")
            kwargs['selected_base_page'] = 'base_lectures.html'
        elif self.content.category.section == '상품':
            print("상품선택")
            kwargs['selected_base_page'] = 'base_products.html'
        return super().get_context_data(**kwargs)

    def get_queryset(self):

        self.content = get_object_or_404(Content, pk=self.kwargs.get('pk'))
        queryset = self.content.appraisal_set.order_by('-created_at')
        print(str(queryset))

        return queryset


class ContentVideoView(ListView):
    template_name = 'products/content_video.html'
    model = ReplyChapter
    paginate_by = 5
    context_object_name = 'reply_list'

    def get_context_data(self, **kwargs):
        print("ContentVideoView is started")
        ##########################################################
        # paginator의 오브젝트를 context 데이터에서 갖고 온다.
        context = super().get_context_data(**kwargs)
        #print("context : "+str(context))
        paginator = context['paginator']
        print(paginator)
        ##########################################################

        # pagenator의 페이지당 인덱스 수를 5로 설정한다.
        page_numbers_range = 5  # Display only 5 page numbers
        # set max_index as "int" from the length of paginator.page_range
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        # python if syntax check!
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        #########next index checking and last index setting#######
        if end_index >= max_index:
            end_index = max_index
            has_next_index = False
        else:
            has_next_index = True

        ####################previous index checking###############
        if (start_index + 1) > 1:
            has_previous_index = True
        else:
            has_previous_index = False

        page_range = paginator.page_range[start_index:end_index]
        print("page_range type : " + str(type(page_range)))
        print("page_range : " + str(page_range))
        print("page_range len : " + str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index + 1) - page_numbers_range
        print((start_index + 1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        try:
            selected_user = self.content.userprofile_set.get(user=self.request.user)
            if (selected_user is not None):
                kwargs['isRegistered'] = True
                print(selected_user)
                print("등록된 사용자")

        except:
            print("등록안된 사용자")
            kwargs['isRegistered'] = False

        kwargs['content'] = self.content
        kwargs['video'] = self.video
        if self.content.category.section == '강좌':
            print("강좌선택")
            kwargs['selected_base_page'] = 'base_lectures.html'
        elif self.content.category.section == '상품':
            print("상품선택")
            kwargs['selected_base_page'] = 'base_products.html'

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        print("ContentVideoView is started in get_queryset")
        self.content = get_object_or_404(Content, pk=self.kwargs.get('pk'))
        self.video = get_object_or_404(Video, pk=self.kwargs.get('pk_video'))
        reply_list = self.video.replychapter_set.order_by('-order')
        queryset = reply_list

        return queryset



@login_required(login_url="accounts:login")
def content_review_add_view(request, pk):
    print("content_review_add_view is started")
    content = get_object_or_404(Content, pk=pk)
    appraisal_list = content.appraisal_set.order_by('-created_at')

    if request.method == 'POST':
        form = AppraisalForm(request.POST)
        if form.is_valid():
            appraisal = form.save(commit=False)
            appraisal.content = content
            appraisal.user = request.user
            appraisal.save()
            return redirect('products:content_review',
                            pk=pk
                            )
    else:
        if content.category.section == '강좌':
            print("강좌선택")
            selected_base_page = 'base_lectures.html'
        elif content.category.section == '상품':
            print("상품선택")
            selected_base_page = 'base_products.html'
        form = AppraisalForm()

    return render(request, 'products/content_review_add.html',
                  {'content': content,
                   'appraisal_list': appraisal_list,
                   'form': form,
                   'selected_base_page': selected_base_page,
                   })


@login_required(login_url="accounts:login")
def content_review_remove_view(request, pk, pk_appraisal):
    print("content_review_remove_view is started")
    content = get_object_or_404(Content, pk=pk)
    appraisal = get_object_or_404(Appraisal, pk=pk_appraisal)

    if appraisal.user == request.user:
        try:
            appraisal.delete()
        except:
            print("삭제할 appraisal이 존재하지 않습니다.")

    return redirect('products:content_review', pk=content.pk)





@login_required(login_url="accounts:login")
def video_add_reply_view(request, pk, pk_video):
    print("video_add_reply_view is started")
    content = get_object_or_404(Content, pk=pk)
    video = get_object_or_404(Video, pk=pk_video)
    reply_list = ReplyChapter.objects.filter(video=video).order_by('-order')


    if request.method == 'POST':
        form = ReplyChapterForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.video = video
            reply.order = video.replychapter_set.count()
            reply.user = request.user
            reply.save()
            return redirect('products:content_video',
                            pk=pk, pk_video=pk_video,
                            )
    else:

        form = ReplyChapterForm()

        try:
            selected_user = content.userprofile_set.get(user=request.user)
            if (selected_user is not None):
                isRegistered = True
                print(selected_user)
                print("등록된 사용자")

        except:
            print("등록안된 사용자")
            isRegistered = False

        if content.category.section == '강좌':
            print("강좌선택")
            selected_base_page = 'base_lectures.html'
        elif content.category.section == '상품':
            print("상품선택")
            selected_base_page = 'base_products.html'


    return render(request, 'products/content_video_reply.html',
                  {'content': content,
                   'video': video,
                   'reply_list': reply_list,
                   'form': form,
                   'isRegistered': isRegistered,
                   'selected_base_page': selected_base_page,
                   })



@login_required(login_url="accounts:login")
def video_remove_reply_view(request, pk, pk_video, pk_reply):
    print("video_remove_reply_view is started")
    #content = get_object_or_404(Content, pk=pk)
    video = get_object_or_404(Video, pk=pk_video)
    selected_reply = get_object_or_404(ReplyChapter, pk=pk_reply)
    reply_list = ReplyChapter.objects.filter(video=video).order_by('-order')


    if selected_reply.user == request.user:
        print("reply.user == request.user")
        try:
            for reply_one in reply_list:
                if reply_one.order > selected_reply.order:
                    print(str(reply_one.order))
                    reply_one.order -= 1
                    reply_one.save()

        except:
            print("It is the highest order.")

        try:
            selected_reply.delete()
            print("Reply deletion success")
        except:
            print("Reply deletion error")

    return redirect('products:content_video',
                    pk=pk,
                    pk_video=pk_video,
                    )


@login_required(login_url="accounts:login")
def video_edit_reply_view(request, pk, pk_video, pk_reply):
    print("video_edit_reply_view is started")
    content = get_object_or_404(Content, pk=pk)
    video = get_object_or_404(Video, pk=pk_video)
    reply_list = ReplyChapter.objects.filter(video=video).order_by('-order')
    reply_order = ReplyChapter.objects.get(pk=pk_reply).order

    # 수정을 위한 해당 Post ritrieve 과정
    selected_reply = get_object_or_404(ReplyChapter, pk=pk_reply)
    # 해당 Post정보를 이용해서 form구성
    form = ReplyChapterForm(request.POST or None, instance=selected_reply)

    # print(queryset)
    reply_for_page = 5
    number_for_page = (reply_list.count() - reply_order) / reply_for_page
    number_for_page_int = int(number_for_page)
    if number_for_page_int < number_for_page:
        number_for_page = int(number_for_page) + 1
    else:
        number_for_page = int(number_for_page)

    print(str(number_for_page))
    queryset = reply_list
    page = request.GET.get('page', number_for_page)
    current_page = number_for_page
    paginator = Paginator(queryset, reply_for_page)

    # pagenator의 페이지당 인덱스 수를 5로 설정한다.
    page_numbers_range = 5  # Display only 5 page numbers
    # set max_index as "int" from the length of paginator.page_range
    # print(type(paginator.page_range))
    # print(type(len(paginator.page_range)))
    max_index = len(paginator.page_range)

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    print("start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range")
    print("{0} = int(({1} - 1) / {2}) * {3}".format(start_index, current_page, page_numbers_range, page_numbers_range))
    end_index = start_index + page_numbers_range
    print(end_index)

    ####next index checking and last index setting#####
    if end_index >= max_index:
        end_index = max_index
        has_next_index = False
    else:
        has_next_index = True

    ####previous index checking#####
    if (start_index + 1) > 1:
        has_previous_index = True
    else:
        has_previous_index = False

    page_range = paginator.page_range[start_index:end_index]
    next_index = start_index + page_numbers_range + 1
    previous_index = (start_index + 1) - page_numbers_range

    if request.method == 'POST':
        print("form POST 성공")
        if form.is_valid():
            reply = form.save(commit=False)
            reply.updated_at = timezone.now()
            reply.save()
            print("form 저장 성공")

            ##########################################################
            number_for_page = (reply_list.count() - reply_order) / reply_for_page
            number_for_page_int = int(number_for_page)
            if number_for_page_int < number_for_page:
                number_for_page = int(number_for_page) + 1
            else:
                number_for_page = int(number_for_page)

            ##########################################################

            base_url = reverse('products:content_video',
                               kwargs={
                                   'pk': pk,
                                   'pk_video': pk_video,
                               })
            query_string = urlencode({'page': number_for_page})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
    else:
        #form = ReplyChapterForm(request.POST or None, instance=selected_reply)

        try:
            reply_list = paginator.page(page)
        except PageNotAnInteger:
            # fallback to the first page
            reply_list = paginator.page(1)
        except EmptyPage:
            # probably the user tried to add a page number
            # in the url, so we fallback to the last page
            reply_list = paginator.page(paginator.num_pages)

        try:
            selected_user = content.userprofile_set.get(user=request.user)
            if (selected_user is not None):
                isRegistered = True
                print(selected_user)
                print("등록된 사용자")

        except:
            print("등록안된 사용자")
            isRegistered = False

        if content.category.section == '강좌':
            print("강좌선택")
            selected_base_page = 'base_lectures.html'
        elif content.category.section == '상품':
            print("상품선택")
            selected_base_page = 'base_products.html'

    return render(request, 'products/content_video_reply_edit.html',
                  {'content': content,
                   'video': video,
                   'reply_list': reply_list,
                   'pk_reply': pk_reply,
                   'form': form,
                   'page_range': page_range,
                   'next_index': next_index,
                   'previous_index': previous_index,
                   'has_next_index': has_next_index,
                   'has_previous_index': has_previous_index,
                   'isRegistered': isRegistered,
                   'selected_base_page': selected_base_page,
                   }
                  )

@login_required(login_url="accounts:login")
def video_reply_to_reply_view(request, pk, pk_video, pk_reply):
    print("video_reply_to_reply_view is started")
    content = get_object_or_404(Content, pk=pk)
    video = get_object_or_404(Video, pk=pk_video)
    reply_list = ReplyChapter.objects.filter(video=video).order_by('-order')
    reply_order = ReplyChapter.objects.get(pk=pk_reply).order

    # print(queryset)
    reply_for_page = 5
    number_for_page = (reply_list.count() - reply_order) / reply_for_page
    number_for_page_int = int(number_for_page)
    if number_for_page_int < number_for_page:
        number_for_page = int(number_for_page) + 1
    else:
        number_for_page = int(number_for_page)

    print(str(number_for_page))
    queryset = reply_list
    page = request.GET.get('page', number_for_page)
    current_page = number_for_page
    paginator = Paginator(queryset, reply_for_page)

    # pagenator의 페이지당 인덱스 수를 5로 설정한다.
    page_numbers_range = 5  # Display only 5 page numbers
    # set max_index as "int" from the length of paginator.page_range
    # print(type(paginator.page_range))
    # print(type(len(paginator.page_range)))
    max_index = len(paginator.page_range)

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    print("start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range")
    print("{0} = int(({1} - 1) / {2}) * {3}".format(start_index, current_page, page_numbers_range, page_numbers_range))
    end_index = start_index + page_numbers_range
    print(end_index)

    ####next index checking and last index setting#####
    if end_index >= max_index:
        end_index = max_index
        has_next_index = False
    else:
        has_next_index = True

    ####previous index checking#####
    if (start_index + 1) > 1:
        has_previous_index = True
    else:
        has_previous_index = False

    page_range = paginator.page_range[start_index:end_index]
    next_index = start_index + page_numbers_range + 1
    previous_index = (start_index + 1) - page_numbers_range

    if request.method == 'POST':
        print("form POST 성공")
        form = ReplyChapterForm(request.POST)
        if form.is_valid():
            try:
                for reply_one in reply_list:
                    if reply_one.order >= reply_order:
                        print(str(reply_one.order))
                        reply_one.order += 1
                        reply_one.save()

            except:
                print("It is the highest order.")

            reply = form.save(commit=False)
            reply.video = video
            reply.order = reply_order
            reply.user = request.user
            reply.is_reply_to_reply = True
            reply.reply_to_reply_address = pk_reply
            reply.save()
            print("form 저장 성공")

            ##########################################################
            number_for_page = (ReplyChapter.objects.filter(video=video).count() - reply_order) / reply_for_page
            number_for_page_int = int(number_for_page)
            if number_for_page_int < number_for_page:
                number_for_page = int(number_for_page) + 1
            else:
                number_for_page = int(number_for_page)

            ##########################################################

            base_url = reverse('products:content_video',
                               kwargs={
                                   'pk': pk,
                                   'pk_video': pk_video,
                               })
            query_string = urlencode({'page': number_for_page})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
    else:
        form = ReplyChapterForm()

        try:
            reply_list = paginator.page(page)
        except PageNotAnInteger:
            # fallback to the first page
            reply_list = paginator.page(1)
        except EmptyPage:
            # probably the user tried to add a page number
            # in the url, so we fallback to the last page
            reply_list = paginator.page(paginator.num_pages)

        try:
            selected_user = content.userprofile_set.get(user=request.user)
            if (selected_user is not None):
                isRegistered = True
                print(selected_user)
                print("등록된 사용자")

        except:
            print("등록안된 사용자")
            isRegistered = False

        if content.category.section == '강좌':
            print("강좌선택")
            selected_base_page = 'base_lectures.html'
        elif content.category.section == '상품':
            print("상품선택")
            selected_base_page = 'base_products.html'

    return render(request, 'products/content_video_reply_to_reply.html',
                  {'content': content,
                   'video': video,
                   'reply_list': reply_list,
                   'pk_reply': pk_reply,
                   'form': form,
                   'page_range': page_range,
                   'next_index': next_index,
                   'previous_index': previous_index,
                   'has_next_index': has_next_index,
                   'has_previous_index': has_previous_index,
                   'isRegistered': isRegistered,
                   'selected_base_page': selected_base_page,
                   }
                  )