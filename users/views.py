from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from users.forms import UserForm, UserProfileForm
from users.models import UserProfile
from users.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from manager.models import Manager
from waiter.models import Waiter
from bartender.models import Bartender
from django.db import connection
# Create your views here.


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'],
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print("%s, %s, %s" %(user.username, user.email, user.password))
                    cursor = connection.cursor()
                    if Manager.objects.filter(
                            manager__email=user.email).exists():
                        return redirect('/manager/')
                    if Bartender.objects.filter(
                            bartender__email=user.email).exists():
                        return redirect('/bartender/')
                    if Waiter.objects.filter(
                            waiter__email=user.email).exists():
                        return redirect('/waiter/')

                else:
                    return redirect("/logout/")

            else:
                return redirect("/logout/")

    else:
        form = LoginForm(data=request.POST)
    variables = RequestContext(request, {'form': form})

    return render_to_response('login_form.html', variables,)
