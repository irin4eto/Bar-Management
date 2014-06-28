from django import forms
from orders.models import StatusOrders

CHOICES = (StatusOrders.objects.values_list('items', 'amount'))


class WaitingOrdersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(WaitingOrdersForm, self).__init__(*args, **kwargs)
        self.fields['choices_waiting_orders'] = forms.ModelMultipleChoiceField(
            to_field_name='id',
            queryset=StatusOrders.objects.filter(status="W"),
            widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = StatusOrders
        fields = ('choices_waiting_orders',)


class AdoptedOrdersForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AdoptedOrdersForm, self).__init__(*args, **kwargs)
        self.fields['choices_adopted_orders'] = forms.ModelMultipleChoiceField(
            to_field_name='id',
            queryset=StatusOrders.objects.filter(status="A"),
            widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = StatusOrders
        fields = ('choices_adopted_orders',)









