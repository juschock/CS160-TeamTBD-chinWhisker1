from django import forms
from datetime import date

RAZORS = ((0, 'Eletric - plug'), (1, 'Electric - Battery'), (2, 'Electric-Dual'),
          (3, 'Blade'), (4, 'Razor'), (5, 'Other'))

class ShaverForm(forms.Form):
    id = forms.IntegerField(widget = forms.HiddenInput(), required = False)
    brand = forms.CharField()
    model = forms.CharField()
    # color = forms.CharField()
    type = forms.ChoiceField(choices=RAZORS)
    qty = forms.IntegerField(min_value=1,max_value=100)
    shave_image = forms.URLField()
    # Override the default field order, which is the declaration order
    field_order = ['brand', 'model', 'type', 'qty', 'color', 'shave_image']

def searchRazorsForKey(value):
    for element in RAZORS:
        if(value in element):
            return element[0]
    return -1