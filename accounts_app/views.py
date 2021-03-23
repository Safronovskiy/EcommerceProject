from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AuthUserRegisterForm, LoginForm
from .models import AuthUserModel
from django.contrib import messages
from django.conf import settings




def registration_view(request):
    if request.method == 'POST':
        form = AuthUserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(raw_password=form.cleaned_data['password1'])
            user.save()
            # AuthUserModel.objects.create_user(email=form.cleaned_data['email'],
            #                                 username=form.cleaned_data['username'],
            #                                 password=form.cleaned_data['password1'],
            #                                 phone=form.cleaned_data['phone'],
            #                                 first_name=form.cleaned_data['first_name'],
            #                                 last_name=form.cleaned_data['last_name'])
            return redirect('accounts_app:login')
        else:
            form = AuthUserRegisterForm(data=request.POST)
            mess = messages.error(request, 'Введены неверные данные')
            return render(request, 'registration.html', {'form': form, 'messages':mess})
    form = AuthUserRegisterForm()
    return render(request, 'registration.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                print(request.path)
                return redirect('accounts_app:profile')
            else:
                messages.error(request, 'Такого пользователя не существует.')
                form = LoginForm(data=request.POST)
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Введены некорректные данные.')
            form = LoginForm(data=request.POST)
            return render(request, 'login.html', {'form': form})
    form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shop_app:start')
    else:
        return render(request, 'logout_confirmation.html')



@login_required()
def profile_view(request):
    return render(request, 'profile.html',{})




















#----------------------------------------------------------CBV------------------------------------------------------
#
# class UserRegisterView(CreateView):
#     template_name = 'registration.html'
#     form_class = AuthUserRegisterForm
#     context_object_name = 'reg_form'
#     success_url = reverse_lazy('accounts_app:login')
















