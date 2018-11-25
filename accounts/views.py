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

from accounts.models import UserProfile

from accounts.forms import (
    LoginForm,
    #    PasswordChangeForm,
    RegistrationForm,
    UserEditForm,
    ProfileEditForm
)


# --TemplateView

class AccountsIndexView(TemplateView):
    template_name = 'accounts/index.html'

    @login_required(login_url="accounts:login")
    def get_user_state(self):
        if self.request.is_authenticate:
            print("로그인된 경우")

    def get_context_data(self, **kwargs):  # get_context_data method 정의시, super() method 반드시 호출!
        context = super().get_context_data(**kwargs)
        context['model_list'] = UserProfile.objects.all()

        return context


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
                ##authenticate doesn't allow the user with not is_active  Django 1.10
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


def register_view(request):
    ################로그인 된 경우 redirect######################
    if auth.get_user(request).is_authenticated:
        next = request.GET.get('next', '/')  # next 기능은 작동 안됨
        return redirect(next)
    ##########################################################

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # UserProfile.objects.create(user=new_user) #now it linked to User.model
            # log the user in
            login(request, new_user)
            # previous 페이지로 redirect 할 수 있도록 코드 작성
            # prev_page= request.META.get('HTTP_REFERER')
            # print('register_view to previous url - '+prev_page)
            # return HttpResponseRedirect(prev_page)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register_form.html', args)


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


#def password_reset(request):
#    pass


#def password_reset_done(request):
#    pass


#def password_reset_confirm(request):
#    pass


#def password_reset_complete(request):
#    pass
