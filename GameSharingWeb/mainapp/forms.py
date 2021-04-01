from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label='Дата получения заказа'

    #order_date = forms.DateField(widget=forms.TextInput(attrs={'type' : 'date'}))

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        ]
        widgets = {
            'order_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
