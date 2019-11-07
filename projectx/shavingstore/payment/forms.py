from django import forms
from datetime import date
import re

CARD_TYPES = ((0, 'American Express'), (1, 'Discover'),
              (2, 'Mastercard'), (3, 'Visa'))


class PaymentForm(forms.Form):
    card_number = forms.CharField()
    card_type = forms.ChoiceField(choices=CARD_TYPES)
    billing_address = forms.CharField()
    # Override the default field order, which is the declaration order
    field_order = ['card_type', 'card_number', 'billing_address']

    # This validator is invoked when is_valid() gets invoked
    def clean_card_number(self):
        error = False
        # Get the selected card type
        selected_card_type = CARD_TYPES[int(self.cleaned_data['card_type'])][1]
        # Get the field value from cleaned_data dict
        value = self.cleaned_data['card_number']
        # Check if the value is valid
        if(selected_card_type == 'American Express' and re.search(r"^3[47][0-9]{13}$", value) is None):
            error = True
        if(selected_card_type == 'Discover' and re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", value) is None):
            error = True
        if(selected_card_type == 'Mastercard' and
           re.search(r"^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$", value) is None):
            error = True
        if(selected_card_type == 'Visa' and re.search(r"^4[0-9]{12}(?:[0-9]{3})?$", value) is None):
            error = True
        # Raise error
        if(error == True):
            raise forms.ValidationError(
                "Please enter a valid card number", code='cardnumber')
        # Always return value
        return value

class EditPaymentForm(forms.Form):
    id = forms.IntegerField(widget = forms.HiddenInput(), required = False)
    card_number = forms.CharField(widget = forms.HiddenInput(), required = False)
    card_type = forms.CharField(widget = forms.HiddenInput(), required = False)
    billing_address = forms.CharField()
    # Override the default field order, which is the declaration order
    field_order = ['card_type', 'card_number', 'billing_address']