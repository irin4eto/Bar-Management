from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from orders.models import Stock, StatusOrders, Sales
from waiter.tableOrders import TableOrders
from django.views.decorators.csrf import csrf_protect
from django.db import connection
from waiter.models import Waiter
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import F


@csrf_protect
@login_required
def waiter(request):
    table = TableOrders(Stock.objects.all())
    print(Stock.objects.all())
    RequestConfig(request).configure(table)

    if request.method == "POST":
        selected_id = request.POST.getlist("selection")
        amount = request.POST.getlist("amount")

        cursor = connection.cursor()
        placeholder = '?'
        placeholders = ', '.join(placeholder for unused in selected_id)
        query = 'SELECT name FROM orders_stock WHERE id IN (%s)' % placeholders
        selected_order = cursor.execute(query, selected_id).fetchall()

        print(amount)
        print(selected_id)
        print(request.user)
        print(selected_order)
        if len(selected_order) == 0:
            return redirect('/waiters/')
        if len(selected_order) == 1:
            order_item = selected_order[0][0]
            order_amount = amount[int(selected_id[0]) - 1]
        else:
            order_item = ""
            order_amount = ""
            index_amount = 0
            for item in selected_order:
                order_item = order_item + "%s, " % item[0]
                order_amount = order_amount + "%s, " % amount[
                    int(selected_id[index_amount]) - 1]
                index_amount += 1

        status_order = StatusOrders(items=order_item,
                                    amount=order_amount,
                                    status="W",
                                    waiter=request.user.username,
                                    bartender="")
        status_order.save()

        index_amount = 0
        for item in selected_order:
            order_item = item[0]
            count = int(amount[int(selected_id[index_amount]) - 1])
            query = 'SELECT * FROM orders_stock WHERE name = %s' % order_item
            stock = Stock.objects.get(name=order_item)
            if Sales.objects.filter(item=stock).exists():
                status_orders = Sales.objects.get(item=stock)
                status_orders.count = F('count') + count
                status_orders.save()
            else:
                status_orders = Sales(item=stock, count=count)
                status_orders.save()

    return render(request, 'waiter.html', {'table': table})
