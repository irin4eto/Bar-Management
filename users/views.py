from django.shortcuts import redirect, render
from django.contrib.auth import views
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from users.forms import UserForm, UserProfileForm
from users.models import UserProfile
# Create your views here.


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
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
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('create_user.html',
                              {'user_form': user_form,
                               'profile_form': profile_form,
                               'registered': registered},
                              context)



