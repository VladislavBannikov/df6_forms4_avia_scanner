from django import forms

from .widgets import AjaxInputWidget
from .models import City

city_api = "/api/city_ajax"
attrs = {'class': 'inline right-margin'}


class SearchTicket(forms.Form):
    to_city = forms.CharField(widget=AjaxInputWidget(city_api, attrs=attrs))
    from_city = forms.CharField(widget=AjaxInputWidget(city_api, attrs=attrs))
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
