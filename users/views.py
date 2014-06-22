from django.shortcuts import redirect, render
from django.contrib.auth import views
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from users.forms import UserForm, UserProfileForm
from users.models import UserProfile
from users.forms import LoginForm
from users.models import create_user_profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    print("The username or password were incorrect.")
            else:
                print("The username or password were incorrect.")
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm(data=request.POST)
    variables = RequestContext(request, {'form': form})

    return render_to_response('login_form.html', variables,)


def manager(request):
    if request.method == 'POST':
        if "create_user" in request.POST:
            return redirect('create_user')
    return render(request, "manager_choices.html", locals())

@csrf_protect
def create_user(request):
    if request.method == 'POST':
        uform = UserForm(data=request.POST)
        pform = UserProfileForm(data=request.POST)

        if uform.is_valid() and pform.is_valid():
            new_user = User.objects.create_user(
                username=uform.cleaned_data['username'],
                email=uform.cleaned_data['email'],
                password=uform.cleaned_data['password1'],
                first_name=uform.cleaned_data['first_name'],
                last_name=uform.cleaned_data['last_name'])
            user_profile = UserProfile(
                user=new_user,
                role=pform.cleaned_data['role']
                )
            """role=uform.cleaned_data['role'],
            first_name=uform.cleaned_data['first_name'],
            last_name=uform.cleaned_data['last_name'])"""
            user_profile.save()
            return HttpResponseRedirect('/manager/')

    else:
        uform = UserForm(data=request.POST)
        pform = UserForm(data=request.POST)
    variables = RequestContext(request, {
        'uform': uform,
        'pform': pform
    })

    return render_to_response('create_user.html',

                              variables)



