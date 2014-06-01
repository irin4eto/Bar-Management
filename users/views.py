from django.shortcuts import redirect, render
from django.contrib.auth import views
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/%s/' % (user.role.lower()))
            else:

                return HttpResponse("Your account is disabled.")
        else:

            print("Invalid login details: {0}, {1}".format(email, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login_form.html', {}, context)


def manager(request):
    if request.method == 'POST':
        if "create_user" in request.POST:
            return redirect('create_user')
    return render(request, "manager_choices.html", locals())


def create_user(request):
    return render(request, "create_user.html", locals())


