from .models import Order
from django import forms


class orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['order_id','user']