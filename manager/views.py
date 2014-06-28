from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.forms import UserForm, UserProfileForm
from manager.models import Manager
from waiter.models import Waiter
from bartender.models import Bartender
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from orders.models import StatusOrders, Sales


@login_required
def manager(request):
    if request.method == 'POST':
        if "create_user" in request.POST:
            return redirect('create_user')
        if "check_sales" in request.POST:
            return redirect('check_sales')
    return render(request, "manager.html", locals())


@login_required
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
            role = pform.cleaned_data['role']
            if role == 'M':
                manager = Manager(manager=new_user)
                manager.save()
            if role == 'W':
                waiter = Waiter(waiter=new_user)
                waiter.save()
            if role == 'B':
                bartender = Bartender(bartender=new_user)
                bartender.save()
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


def check_sales(request):
    sales = Sales.objects.all()
    return render_to_response('check_sales.html',
                              {'sales': sales})
