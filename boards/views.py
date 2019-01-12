from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
    CreateView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from accounts.models import UserProfile
from boards.models import Board, Post, Topic
from django.contrib.auth.models import User
from boards.forms import NewContentForm, NewPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from boards.forms import (
    NewPostForm,
    NewContentForm
)
from urllib.parse import urlencode

# Create your views here.

# def home(request)
class BoardsIndexView(TemplateView):
    # print("BoardsIndexView is started")
    template_name = 'boards/index.html'

    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
        print("BoardsIndexView is started")
        context = super().get_context_data(**kwargs)


        board1=Board.objects.get(pk=1).topic.order_by('-updated_at')
        #print(type(board1))
        #print(board1.all().first())
        board2=Board.objects.get(pk=2).topic.order_by('-updated_at')
        #print(type(board2))
        #print(board2.all().first())
        board3=Board.objects.get(pk=3).topic.order_by('-updated_at')
        #print(type(board3))
        #print(board3.all().first())

        board_list = [board1, board2, board3]
        context['board_list'] = board_list
        #print(board1.all().first().user)
        #print(board_list)
        #context['topic_list'] = Topic.objects.
        # user = auth.get_user(self.request)
        # user_profile = UserProfile.objects.get(user__username=user)
        # context = {'user':user, 'user_profile':user_profile}

        return context

    #def get_queryset(self):
     #   self.board = get_object_or_404(Board, pk=1)
     #   queryset = self.board.topic.order_by('-updated_at')
     #   return queryset

# topic list를 보여주는 function view
#def board_content_list_view(request, pk):
#    print("board_content_list_view is started")
#    board = get_object_or_404(Board, pk=pk)
#    queryset = board.topic.order_by('-updated_at')
#    page = request.GET.get('page', 1)
#
#    paginator = Paginator(queryset, 10)
#
#    try:
#        topics = paginator.page(page)
#    except PageNotAnInteger:
#        # fallback to the first page
#        topics = paginator.page(1)
#    except EmptyPage:
#        # probably the user tried to add a page number
#        # in the url, so we fallback to the last page
#        topics = paginator.page(paginator.num_pages)
#
#    return render(request, 'boards/board_list.html', {'board': board, 'topic_list': topics})

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topic_list'
    template_name = 'boards/board_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        print("TopicListView is started")
        print("board pk is :" + str(self.board.pk))
        kwargs['board'] = self.board

        ##########################################################
        # paginator의 오브젝트를 context 데이터에서 갖고 온다.
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        print(paginator)
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
        print("start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range")
        print("{0} = int(({1} - 1) / {2}) * {3}".format(start_index, current_page, page_numbers_range,
                                                        page_numbers_range))
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
        print("page_range type : " + str(type(page_range)))
        print("page_range : " + str(page_range))
        print("page_range len : " + str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index + 1) - page_numbers_range
        print((start_index + 1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        ##########################################################

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topic.order_by('-updated_at')
        return queryset


# topic list를 보여주는 class view 사용하지 않음
#class BoardsTopicView(DetailView):
    # print("BoardsTopicView is started")
#    template_name = 'boards/board_list.html'
#    model = Board
#    paginate_by = 6

    ##DetailView는 PK같은 인자를 받아서 처리하기 때문에 인자와
    ##연관된 object를 queryset으로 지정해야지 된다.
    ##만약 queryset에 등록된 게시물이 (topic) 2개 인경우,
    ##board가 4개라고 하더라도 no query로 404error가 나타날 수 있다.
    # context_object_name = 'topic_list'
    # queryset = Topic.objects.all()

#    def get_context_data(self, **kwargs):
#        print("BoardsTopicView is started")
#        context = super().get_context_data(**kwargs)
#        try:
#            user = auth.get_user(self.request)
#            number = self.kwargs.get(self.pk_url_kwarg)
#            print("보드 게시판 pk : "+number)
#
#            board = Board.objects.get(pk=number)
#            print(board)
#            topic_list = Topic.objects.filter(board=board).order_by('-updated_at')
#            context['topic_list'] = topic_list
#            context['board'] = board

#        except:
#            pass

#        return context


class BoardsContentView(ListView):
    template_name = 'boards/board_content.html'
    context_object_name = 'post_list'
    model = Post

    paginate_by = 10

    def get_context_data(self, **kwargs):
        print("BoardsContentView is started")
        print("topic pk is :" + str(self.topic.pk))
        session_key = 'viewed_topic_{}'.format(self.topic.pk)
        context = super().get_context_data(**kwargs)
        ##########################################################
        #paginator의 오브젝트를 context 데이터에서 갖고 온다.
        paginator = context['paginator']
        print(paginator)
        #pagenator의 페이지당 인덱스 수를 5로 설정한다.
        page_numbers_range = 5  # Display only 5 page numbers
        #set max_index as "int" from the length of paginator.page_range
        #print(type(paginator.page_range))
        #print(type(len(paginator.page_range)))
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        #python if syntax check!
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        print("start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range")
        print("{0} = int(({1} - 1) / {2}) * {3}".format(start_index,current_page,page_numbers_range,page_numbers_range))
        end_index = start_index + page_numbers_range
        print(end_index)

        ####next index checking and last index setting#####
        if end_index >= max_index:
            end_index = max_index
            has_next_index = False;
        else:
            has_next_index = True;

        ####previous index checking#####
        if (start_index+1) > 1 :
            has_previous_index = True
        else:
            has_previous_index = False



        page_range = paginator.page_range[start_index:end_index]
        print("page_range type : "+str(type(page_range)))
        print("page_range : "+str(page_range))
        print("page_range len : "+str(len(page_range)))
        kwargs['page_range'] = page_range
        kwargs['next_index'] = start_index + page_numbers_range + 1
        kwargs['previous_index'] = (start_index+1) - page_numbers_range
        print((start_index+1) - page_numbers_range)
        kwargs['has_next_index'] = has_next_index
        kwargs['has_previous_index'] = has_previous_index

        ##########################################################




        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True

        kwargs['board'] = self.board
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)


    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.post.order_by('-order')
        return queryset



# topic과 post list를 보여주는 보여주는 function view 사용하지 않음
#def see_content_view(request, pk, topic_pk):
#    board = get_object_or_404(Board, pk=pk)
#    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
#    post = topic.post.all().order_by('-order')

#    topic.views += 1;
#    topic.save()
#     user = User.objects.get(username=request.user)

#    return render(request, 'boards/board_content.html', {'board': board, 'topic': topic, 'post_list': post})

# 페이지네이션이 필요 없음.
@login_required(login_url="accounts:login")
def add_content_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.get(username=request.user)  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewContentForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.user = user
            topic.updated_at = timezone.now()
            topic.save()

            return redirect('boards:board_topic', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewContentForm()
    return render(request, 'boards/board_write_form.html', {'board': board, 'form': form})

# 페이지네이션이 필요 없음.
@login_required(login_url="accounts:login")
def edit_content_view(request, pk, topic_pk):
    print('edit_content_view')
    board = get_object_or_404(Board, pk=pk)
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    form = NewContentForm(request.POST or None, instance=topic)



    if request.method == 'POST':

        if form.is_valid():
            topic = form.save(commit=False)
            topic.updated_at = timezone.now()
            topic.save()

            return redirect('boards:board_content', pk=board.pk,
                            topic_pk=topic_pk)  # TODO: redirect to the created topic page
    else:
        form = NewContentForm(instance=topic)
    return render(request, 'boards/board_content_edit.html', {'board': board,
                                                              'topic' : topic,
                                                              'form': form})

# 페이지네이션이 필요 없음.
@login_required(login_url="accounts:login")
def remove_content_view(request, pk, topic_pk):
    board = get_object_or_404(Board, pk=pk)
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if topic.user == request.user:
        try:
            topic.delete()
        except:
            print("삭제할 Topic이 존재하지 않습니다.")

    return redirect('boards:board_topic', pk=board.pk)


#작동안됨......
class AddReplyView(CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'boards/board_reply_content.html'
    #success_url = reverse_lazy('boards:')

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        kwargs['post_list'] = self.topic.post.all()
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        print(self.board)
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        print(self.topic)
        queryset = self.topic.post.order_by('-order')
        return queryset

    def form_invalid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)




# 페이지네이션이 필요.
@login_required(login_url="accounts:login")
def add_reply_view(request, pk, topic_pk):
    board = get_object_or_404(Board, pk=pk)
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    post_list = Post.objects.filter(topic=topic).order_by('-order')

    queryset = topic.post.order_by('-order')
    print(queryset)
    page = request.GET.get('page', 1)
    current_page = int(page) if page else 1
    paginator = Paginator(queryset, 10)

    # pagenator의 페이지당 인덱스 수를 5로 설정한다.
    page_numbers_range = 5  # Display only 5 page numbers
    # set max_index as "int" from the length of paginator.page_range
    # print(type(paginator.page_range))
    # print(type(len(paginator.page_range)))
    max_index = len(paginator.page_range)

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    print("start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range")
    print("{0} = int(({1} - 1) / {2}) * {3}".format(start_index, current_page, page_numbers_range, page_numbers_range))
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
    previous_index = (start_index+1) - page_numbers_range


    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.order = topic.post.count()
            post.user = request.user
            post.save()
            return redirect('boards:board_content',
                            pk=pk, topic_pk=topic_pk,
                            )
    else:

        form = NewPostForm()

        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # fallback to the first page
            post_list = paginator.page(1)
        except EmptyPage:
            # probably the user tried to add a page number
            # in the url, so we fallback to the last page
            post_list = paginator.page(paginator.num_pages)


    return render(request, 'boards/board_reply_content.html',
                  {'board': board,
                   'post_list': post_list,
                   'topic': topic,
                   'form': form,
                   'page_range': page_range,
                   'next_index': next_index,
                   'previous_index': previous_index,
                   'has_next_index': has_next_index,
                   'has_previous_index': has_previous_index,
                   })



# 페이지네이션이 필요.
@login_required(login_url="accounts:login")
def add_reply_to_reply_view(request, pk, topic_pk, post_pk):
    print("add_reply_to_reply_view")
    board = get_object_or_404(Board, pk=pk)
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    post_list = Post.objects.filter(topic=topic).order_by('-order')
    post_order = Post.objects.get(pk=post_pk).order


    #print(queryset)
    number_for_page = (topic.post.count() - post_order)/10
    number_for_page_int = int(number_for_page)
    if number_for_page_int < number_for_page:
        number_for_page = int(number_for_page)+1
    else:
        number_for_page = int(number_for_page)

    print(str(number_for_page))
    queryset = topic.post.order_by('-order')
    page = request.GET.get('page', number_for_page)
    current_page = number_for_page
    paginator = Paginator(queryset, 10)

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
        form = NewPostForm(request.POST)
        if form.is_valid():
            try:
                for post_one in post_list:
                    if post_one.order >= post_order:
                        print(str(post_one.order))
                        post_one.order += 1
                        post_one.save()

            except:
                print("It is the highest order.")
            post = form.save(commit=False)
            post.topic = topic
            post.order = post_order
            post.user = request.user
            post.is_post_to_post = True
            post.post_to_post_address = post_pk
            post.save()

            ##########################################################
            number_for_page = (Post.objects.filter(topic=topic).count() - post_order) / 10
            number_for_page_int = int(number_for_page)
            if number_for_page_int < number_for_page:
                number_for_page = int(number_for_page) + 1
            else:
                number_for_page = int(number_for_page)

            ##########################################################

            base_url = reverse('boards:board_content', kwargs={'pk':pk, 'topic_pk':topic_pk})
            query_string = urlencode({'page' : number_for_page})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
    else:
        form = NewPostForm()

        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # fallback to the first page
            post_list = paginator.page(1)
        except EmptyPage:
            # probably the user tried to add a page number
            # in the url, so we fallback to the last page
            post_list = paginator.page(paginator.num_pages)


    return render(request, 'boards/board_reply_to_reply.html',
                  #{'board': board, 'post_list': post, 'topic': topic, 'post_pk': post_pk, 'slug':slug, 'form': form})
                  {'board': board,
                   'post_list': post_list,
                   'topic': topic,
                   'post_pk': post_pk,
                   'form': form,
                   'page_range': page_range,
                   'next_index': next_index,
                   'previous_index': previous_index,
                   'has_next_index': has_next_index,
                   'has_previous_index': has_previous_index,
                   })


# 페이지네이션이 필요.(검증완료)
@login_required(login_url="accounts:login")
def edit_reply_view(request, pk, topic_pk, post_pk):
    print("edit_reply_view")
    board = get_object_or_404(Board, pk=pk)
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    post_list = Post.objects.filter(topic=topic).order_by('-order')
    post_order = Post.objects.get(pk=post_pk).order

    #수정을 위한 해당 Post ritrieve 과정
    post = get_object_or_404(Post, topic__pk=topic_pk, pk=post_pk)
    #해당 Post정보를 이용해서 form구성
    form = NewPostForm(request.POST or None, instance=post)


    # print(queryset)
    number_for_page = (topic.post.count() - post_order) / 10
    number_for_page_int = int(number_for_page)
    if number_for_page_int < number_for_page:
        number_for_page = int(number_for_page) + 1
    else:
        number_for_page = int(number_for_page)

    print(str(number_for_page))
    queryset = topic.post.order_by('-order')
    page = request.GET.get('page', number_for_page)
    current_page = number_for_page
    paginator = Paginator(queryset, 10)

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

    print("edit_reply_view 성공")
    if request.method == 'POST':
        print("form POST 성공")
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.now()
            post.save()
            print("form 저장 성공")

            ##########################################################
            number_for_page = (topic.post.count() - post_order) / 10
            number_for_page_int = int(number_for_page)
            if number_for_page_int < number_for_page:
                number_for_page = int(number_for_page) + 1
            else:
                number_for_page = int(number_for_page)

            ##########################################################


            base_url = reverse('boards:board_content', kwargs={'pk': pk, 'topic_pk': topic_pk})
            query_string = urlencode({'page': number_for_page})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url)
    else:
        form = NewPostForm(instance=post)

        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # fallback to the first page
            post_list = paginator.page(1)
        except EmptyPage:
            # probably the user tried to add a page number
            # in the url, so we fallback to the last page
            post_list = paginator.page(paginator.num_pages)

    return render(request, 'boards/board_reply_content_edit.html',
                  {'board': board,
                   'topic': topic,
                   'post_list': post_list,
                   'post_pk': post_pk,
                   'form': form,
                   'page_range': page_range,
                   'next_index': next_index,
                   'previous_index': previous_index,
                   'has_next_index': has_next_index,
                   'has_previous_index': has_previous_index,
                   }
                  )

# 페이지네이션이 필요 없음.
@login_required(login_url="accounts:login")
def remove_reply_view(request, pk, topic_pk, post_pk):
    board = get_object_or_404(Board, pk=pk)
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    selected_post = get_object_or_404(Post, pk=post_pk, topic__pk=topic_pk)
    post = Post.objects.filter(topic=topic).order_by('-order')
    print("remove_reply_view 성공")
    if selected_post.user == request.user:
        print("remove_reply_view selected_post.created_at == request.user 성공")
        try:
            for post_one in post:
                if post_one.order > selected_post.order:
                    print(str(post_one.order))
                    post_one.order -= 1
                    post_one.save()

        except:
            print("It is the highest order.")
        selected_post.delete()
        print("remove_reply_view 저장 성공")
    return redirect('boards:board_content', pk=pk, topic_pk=topic_pk, )
