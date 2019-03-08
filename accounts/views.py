from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import (
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm
)
from django.contrib.auth import update_session_auth_hash, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.contrib.auth.hashers import check_password
from accounts.tokens import account_activation_token

#from accounts.utils.handle_upload_file import handle_uploaded_file

from django.contrib.auth.models import User
from accounts.models import UserProfile

from accounts.forms import (
    LoginForm,
    #    PasswordChangeForm,
    RegistrationForm,
    RegistrationProfileForm,
    WithdrawalForm,
    UserEditForm,
    ProfileEditForm,
    FindIdForm
)

from cart.cart import Cart
from cart.models import Cart as CM
from cart.forms import CartAddContentForm

import json
from pprint import pprint

from products.models import Content
from orders.models import Order

from decimal import *


# --TemplateView

class AccountsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dash_board.html'


    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        #context['model_list'] = UserProfile.objects.all()

        user = auth.get_user(self.request)
        user_profile = UserProfile.objects.get(user__username=user)
        product_list = user_profile.favorite.filter(category__section="상품")
        lecture_list = user_profile.favorite.filter(category__section="강좌")
        context = {
            'user':user,
            'user_profile':user_profile,
            'product_list':product_list,
            'lecture_list':lecture_list,
                   }

        return context


@login_required(login_url="accounts:login")
def index_view(request):

    print("accounts:index view execute")
    user = auth.get_user(request)
    user_profile = UserProfile.objects.get(user__username=user)
    print(user)
    print(user_profile)
    print(user_profile.favorite_lecture.all())
    print(user_profile.address)
    #print(requested_user.address)
    print(type(user))
    model_list = UserProfile.objects.all()
    #model_list = UserProfile.objects.get(user__username =)


    #return render(request, 'accounts/profile.html', {'model_list': model_list})
    return render(request, 'accounts/dash_board.html', {'user_profile': user_profile, 'user':user})


def login_view(request):
    print("login view execute")
    try:
        # 테스트시 오류 발생
        current_site = Site.objects.get(name='memaker.co.kr')
        #current_site = get_current_site(request)
        print("current_site : ", current_site)
        print("current_site.domain : ", current_site.domain)
    except:
        print("current_site 할당 실패!!!")

    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################

    #messages = ""



    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            print("form is valid")
            # Validation check username, password
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                print("user is not None")
                ##authenticate doesn't allow the user with not is_active from Django 1.10
                if user.is_active:
                    print("user.is_active : " + str(user.is_active))
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    # previous 페이지로 redirect



                    # 만약 Cart session에 물건이 담겨있으면, user db로 저장
                    cart = Cart(request)
                    if cart.isExist() > 0:
                        for item in cart:
                            #로그인 전 cart session에 담긴 품목을 content object로 불러온다.
                            title = item['content']

                            try:
                                content = Content.objects.get(title=title)
                                #content 데이터와 user 데이트를 이용하여 Cart model을 찾아본다.
                                userCart = get_object_or_404(CM, user=user, content=content)
                                print("카트DB에 있는 데이터")

                                #기존 Cart DB에 있는 자료이면 수량을 더해주고 저장한다.
                                userCart.quantity += int(item['quantity'])

                            except:
                                #content 데이터와 user 데이터로 검색해서 해당 Cart 데이터가 없으면 새로 만들어 준다.
                                print("카트DB에 없는 데이터")
                                userCart = CM.objects.create(user=user, content=content)
                                userCart.quantity = int(item['quantity'])
                                userCart.cost = int(item['cost'])

                            #Cart DB에 저장을 한다.
                            userCart.save()
                        #session cart에 있던 내용을 모두 Cart DB로 옮기고 싹 한번 삭제하고, 초기화 한다.
                        cart.clear()
                        cart.__init__(request)

                    #로그인 전 session cart에 데이터가 있던 없던,
                    #Cart DB의 데이터를 user로 필터링해서 userCart로 할당한다.
                    userCart = CM.objects.filter(user=user)

                    #userCart를 이용해서 session cart에 새로 입력해주면서, Cart DB와 동기화기 시작된다.
                    for cartItem in userCart:
                        cart.add(content=cartItem.content,
                                quantity=cartItem.quantity,
                                update_quantity=False)
                    print(cart.isExist)



                    prev_page = request.GET.get('next', '/')
                    print('login_view to previous url - ' + prev_page)
                    return HttpResponseRedirect(prev_page)
                else:
                    # not excutable code
                    print("not user.is_active")
                    messages.error(request, '사용이 정지된 아이디 입니다. 다시 시도해 주세요.')
                    # return HttpResponse('Disabled account')
            else:
                # return HttpResponse('Invalid login')
                print("user is none")
                messages.error(request, '비밀번호 또는 아이디가 맞지 않습니다. 다시 시도해 주세요.')
        else:
            messages.error(request, '비밀번호 또는 아이디를 입력해주세요.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url="accounts:login")
def logout_view(request):
    logout(request)
    next = request.GET.get('next', '/')
    print(next)
    return redirect(next)


###############탈퇴하기 withdrawal view##################
@login_required(login_url="accounts:login")
def withdrawal_view(request):
    print('widthdrawal_view')
    # UserProfile.objects.get(user=request.user)
    if request.method == 'POST':

        form = WithdrawalForm(data=request.POST,
                                 instance=request.user)
        print(str(form))
        password = request.POST.get('password')
        password_cleaned = form.cleaned_data.get('password')
        user = User.objects.get(username=request.user)
        result_comparison = check_password(password, user.password)

        #print("user is " + str(user))
        #print("Input password is " + str(password))
        #print("Input password(cleaned) is " +str(password_cleaned))
        #print("password of the user is " +str(user.password))
        #print("Input password result : " + str(result_comparison))

        if result_comparison:
            #user = form.save()
            user.is_active = False
            user.save()
            update_session_auth_hash(request, user)  # Important!
            #logout(request)
            #messages.success(request, '회원탈퇴가 성공적으로 진행되었습니다.')
            messages = "회원탈퇴가 성공적으로 진행되었습니다."
            return redirect('accounts:withdrawal_done')
        else:
            #messages.error(request, '비밀번호가 올바르지 않습니다.')
            messages = "비밀번호가 올바르지 않습니다."
            form = WithdrawalForm(instance=request.user)


    else:
        form = WithdrawalForm(instance=request.user)
        messages = ""

    return render(request,
                  'accounts/withdrawal_form.html',
                  {'user_form': form,
                   'messages' : messages,
                   })

###############탈퇴하기 성공 시 withdrawal_done_view 시현##################
def withdrawal_done_view(request):
    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################
    return render(request,
                  'accounts/withdrawal_done.html'
                  )



def find_id_view(request):
    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################
    print("====find_id_view execute===")

    if request.method == 'POST':
        form = FindIdForm(request.POST)

        if form.is_valid():
            print("form is valid")
            requested_email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=requested_email)
                print(user)
                return render(request, 'accounts/find_id_done.html', {'user': user})

            except:
                messages.error(request, '회원 가입 정보를 확인 할 수 없습니다.')



        else:
            messages.error(request, '이메일을 입력해주세요.')

    else:
        form = FindIdForm()

    return render(request, 'accounts/find_id_form.html', {'form': form})





def register_view(request):
    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################

    print("====register_view execute===")
    messages = ""

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        form_profile = RegistrationProfileForm(request.POST)

        ##################테스트 프린팅#################
        #username = request.POST.get('username')
        #print("email : " + str(email) + " username " + str(username))

        email = request.POST.get('email')
        agree = request.POST.get('agree')
        print("agree : "+agree)

        try:
            if agree != 'on':
                messages = '정보 제공에 동의하셔야 합니다.'
                print("정보 제공 동의 안함")
                return render(request,
                              'accounts/register_form.html',
                              {'form': form,
                               'form_profile': form_profile,
                               'messages': messages,
                               })
            else:
                messages = ''
                print("정보 제공 동의")
        except:
            print("정보 제공 동의 확인 에러")
            pass


        try:
            user_objects = User.objects.all()
            for user in user_objects:
                if email == user.email:
                    messages ='등록된 이메일 입니다.'
                    print("등록된 이메일 입니다.")
                    return render(request,
                                  'accounts/register_form.html',
                                  {'form': form,
                                   'form_profile': form_profile,
                                   'messages': messages,
                                   })

            messages = ''
            print("사용 가능한 이메일 주소.")
        except:
            print("사용 가능한 이메일 주소 확인 에러")
            pass


        if form.is_valid() and form_profile.is_valid():
            #이메일 인증이 없는 형태의 회원 가입
            #form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return HttpResponseRedirect('/')

            #이메일 인증이 가능한 회원 가입, 이메일을 인증해야 계정이 활성화 됨.
            user = form.save(commit=False)
            user.is_active = False

            user.save()

            #profile_data.route = form_profile.cleaned_data.get('route')
            #form_profile.save()

            try:
                profile_data = user.userprofile
                get_route = form_profile.cleaned_data.get('route')
                get_agree = form_profile.cleaned_data.get('agree')
                if get_route is not "":
                    print("가입경로 선택 : "+str(get_route))
                    profile_data.route = get_route
                    profile_data.agree = get_agree
                    profile_data.save()
                else:
                    print("가입경로 선택 안됨.....")
            except:
                print("가입경로 선택 확인 에러")
                pass

            try:
                #테스트시 오류 발생
                current_site = Site.objects.get(name='memaker.co.kr')
                #current_site = get_current_site(request)
            except:
                print("current_site 할당 실패!!!")

            subject = '가입을 환영합니다. 만들면서 배우는 코딩교육 미메이커입니다. 링크를 이용하여 계정을 활성화하세요.'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message, from_email='openfingers@openfingers.com')
            return redirect('accounts:account_activation_sent')
    else:
        form = RegistrationForm()
        form_profile = RegistrationProfileForm()


    return render(request, 'accounts/register_form.html',  {'form': form,
                                   'form_profile': form_profile,
                                   'messages': messages,
                                   })

def account_activation_sent(request):
    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################
    return render(request, 'accounts/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.userprofile.email_confirmed = True
        user.save()
        user.userprofile.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'accounts/account_activation_invalid.html')



@login_required(login_url="accounts:login")
def profile_view(request):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    user_profile = UserProfile.objects.get(user__username=request.user)
    #print(get_current_site(request))
    args = {'user': request.user, 'user_profile': user_profile}

    cart = Cart(request)
    if cart.isExist() > 0:
        print("카트에 물건이 있습니다.")
        print(cart.cart)
        print(cart.get_total_cost())
        # for item in cart:
        #     item['update_quantity_form'] = CartAddContentForm(
        #         initial={'quantity': item['quantity'],
        #                  'update': True})
        # print(cart)



    return render(request, 'accounts/profile.html', args)


@login_required(login_url="accounts:login")
def edit_profile_view(request):
    print('edit_profile_view')
    # UserProfile.objects.create(user=request.user)
    if request.method == 'POST':

        user_form = UserEditForm(data=request.POST,
                                 instance=request.user)
        # print(str(user_form))
        #print(user_form['first_name'])

        profile_form = ProfileEditForm(
            instance=request.user.userprofile,
            data=request.POST,
            files=request.FILES #use this code if image or etc file to be loaded
        )

        image_ = request.POST.get('image')
        print(str(image_))

        if user_form.is_valid() and profile_form.is_valid():
            # user_profile = UserProfile.objects.get(user=request.user)
            # user_profile.image = profile_form.cleaned_date['image']
            image = profile_form.cleaned_data['image']
            print("is_valid : " + str(image))
            try:
                image_file = request.FILES['image']
                print("is_valid of FILE : " +str(image_file))
                print(image_file.name)
                print(image_file.size)
            except:
                print("Image file is not loaded.....")
            user_form.save()
            profile_form.save()
            return redirect('/accounts/profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.userprofile)

    return render(request,
                  'accounts/profile_edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form
                   })


@login_required(login_url="accounts:login")
def change_password_view(request):
    print("password_change")
    if request.method == 'POST':
        form = PasswordChangeForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })

@login_required(login_url="accounts:login")
def order_status_view(request):
    print("order_status_view")
    user = auth.get_user(request)
    order_list = Order.objects.filter(name=user.first_name)
    #order_title = order_list.first()

    return render(request, 'accounts/order_status.html', {

        'order_list': order_list
    })

##not used for user to change the password
def password_change_done(request):
    pass

# def password_reset(request):
#    pass


# def password_reset_done(request):
#    pass


# def password_reset_confirm(request):
#    pass


# def password_reset_complete(request):
#    pass
