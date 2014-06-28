from django_tables2 import columns
from django_tables2.columns import TemplateColumn
from orders.models import Stock
import django_tables2 as tables

TEMPLATE = """
<input id="amount" maxlength="2" name="amount" type="number"/>
"""


class TableOrders(tables.Table):
    selection = columns.CheckBoxColumn(accessor="pk")
    amount = TemplateColumn(TEMPLATE)

    class Meta:
        model = Stock

