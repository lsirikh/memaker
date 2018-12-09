from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
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
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.contrib.auth.hashers import check_password
from accounts.tokens import account_activation_token

from django.contrib.auth.models import User
from accounts.models import UserProfile

from accounts.forms import (
    LoginForm,
    #    PasswordChangeForm,
    RegistrationForm,
    WithdrawalForm,
    UserEditForm,
    ProfileEditForm,
    FindIdForm
)


# --TemplateView

class AccountsIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dash_board.html'


    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        #context['model_list'] = UserProfile.objects.all()
        user = auth.get_user(self.request)
        user_profile = UserProfile.objects.get(user__username=user)
        context = {'user':user, 'user_profile':user_profile}

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

    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################

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

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #username = request.POST.get('username')
        #email = request.POST.get('email')
        #print("email : " + str(email) + " username " + str(username))

        if form.is_valid():
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
            current_site = get_current_site(request)
            subject = '이메일로 보내진 링크를 이용하여 계정을 활성화하세요.'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('accounts:account_activation_sent')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register_form.html',  {'form': form})

def account_activation_sent(request):
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
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'accounts/account_activation_invalid.html')



@login_required(login_url="accounts:login")
def profile_view(request):
    # UserProfile.objects.get을 통해 싱글 오브젝트 retrive하기
    user_profile = UserProfile.objects.get(user__username=request.user)

    args = {'user': request.user, 'user_profile': user_profile}
    return render(request, 'accounts/profile.html', args)


@login_required(login_url="accounts:login")
def edit_profile_view(request):
    print('edit_profile_view')
    # UserProfile.objects.create(user=request.user)
    if request.method == 'POST':

        user_form = UserEditForm(data=request.POST,
                                 instance=request.user)
        # print(str(user_form))
        # print(user_form['first_name'])
        # print(user_form['email'])
        profile_form = ProfileEditForm(
            instance=request.user.userprofile,
            data=request.POST
            #    files=request.FILES #use this code if image or etc file to be loaded
        )

        if user_form.is_valid() and profile_form.is_valid():
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
