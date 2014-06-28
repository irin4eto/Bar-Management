from orders.models import StatusOrders
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from bartender.forms import WaitingOrdersForm, AdoptedOrdersForm
from django.db import transaction
from django.contrib.auth.decorators import login_required


@login_required
@csrf_protect
def bartender(request):
    response_dict = {}
    if request.method == 'POST':
        if "accept_orders" in request.POST:
            waiting_orders = WaitingOrdersForm(data=request.POST)
            selected_orders_id = list(
                map(int, request.POST.getlist('choices_waiting_orders')))

            for order in selected_orders_id:
                status_orders = StatusOrders.objects.get(
                    id=order)
                status_orders.bartender = request.user.username
                status_orders.status = 'A'
                status_orders.save()
            transaction.commit_unless_managed()

            checking_orders = StatusOrders.objects.values()
            print(checking_orders)

            response_dict['waiting_orders'] = waiting_orders

        if "ready_orders" in request.POST:
            adopted_orders = AdoptedOrdersForm(data=request.POST)
            ready_orders_id = list(
                map(int, request.POST.getlist('choices_adopted_orders')))

            for order in ready_orders_id:
                status_orders = StatusOrders.objects.get(
                    id=order)
                status_orders.status = 'R'
                status_orders.save()
            response_dict['adopted_orders'] = adopted_orders

    else:
        waiting_orders = WaitingOrdersForm()
        adopted_orders = AdoptedOrdersForm()
        response_dict = {'waiting_orders': waiting_orders,
                         'adopted_orders': adopted_orders}
    context_instance = RequestContext(request, response_dict)

    return render_to_response('bartender.html',
                              context_instance=context_instance)




