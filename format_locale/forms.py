from django import forms


class DatePriceForm(forms.Form):
    date = forms.DateField(localize=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, localize=True)