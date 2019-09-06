import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DatePriceForm


def form_view(request):

    if request.method == 'POST':
        form = DatePriceForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            price = form.cleaned_data['price']
            return HttpResponseRedirect(f'/result/?date={date}&price={price}')

    else:
        form = DatePriceForm()
    
    return render(request, 'locale_form.html', {'form': form})


def form_result_view(request):
    
    context = {}

    if request.method == 'GET':
        price_str = request.GET.get('price')
        date_str = request.GET.get('date')

        date  = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        price = float(price_str)

        context['date'] = date
        context['price'] = price
    
    return render(request, 'locale_result.html', context)
