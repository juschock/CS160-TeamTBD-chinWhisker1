from django.shortcuts import render
from . import forms, models
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import sys

# Create your views here.

def cart(request):
    return render(request,'cart/cart.html') 

'''
def pay(request):
    pmt_method_dict = models.fetch_all_pmt_methods_process()

    return render(request,'payment/pay.html', {'pmt_method_dict': pmt_method_dict})
'''
'''
def help(request):
    contact_name = 'Dustin'
    contact_address = {'sector':'#385','city':'Sabody','planet':'Moon'}
    contact_phone = ['123-456-789','987-654-321']
    contact_hours = ((0,'Mon-Thu 7AM-12PM'),(1,'Fri 1PM-5PM'),(2,'Sat-Sun 7AM-10AM'))
    # Package up all variables into a dictionary
    contact_info = {'contact_name':contact_name, 'contact_address':contact_address, 'contact_phone':contact_phone, 'contact_hours':contact_hours}
    return render(request,'payment/help.html', contact_info)
'''
'''
def add_payment(request):
    title = 'Add a new payment method'
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = forms.PaymentForm(request.POST)
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            card_type = forms.CARD_TYPES[int(form.cleaned_data['card_type'])][1]
            billing_address = form.cleaned_data['billing_address']
            
            try:
                models.create_process(card_number, card_type, billing_address)
                action = 'POST_SUCCESSFULL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'POST_FAILED'
            except:
                print("Unexpected error: " + str(sys.exc_info()[0]))
                form.add_error(None,'Unexpected error - Please contact your system administrator')
                action = 'POST_FAILED'
        else:
            action='POST_FAILED'
    else:
        action='GET'
        # Disable auto_id to prevent the form from generating verbose information.
        # Also, we set the initial value to the album image field
        form = forms.PaymentForm(auto_id=False)
    # Reference form instance (bound/unbound) is sent to template for rendering
    return render(request,'payment/payment_form.html',{'action':action,'form':form,'title':title})
'''
'''
def edit_payment(request):
    id = request.POST.get('id','')
    context = {'card_number':'', 'card_type':''}

    # If id doesn't exist, redirect to the homepage
    if(id == ''):
        return HttpResponseRedirect('/payment/#mainsection')
       
    
    title = "Edit payment method"
    # Create an empty form so that Django doesn't complaint
    form = forms.EditPaymentForm()

    if('popup' in id):
        action = ''

        # Clean up the id
        id = id.replace('popup','')

        try:
            # Fetch the payment method from the DB based on the given id, and then populate the fields 
            payment_method = models.fetch_payment_process(id)
            form = forms.EditPaymentForm(auto_id=False, initial={'id':payment_method.id,'card_number':payment_method.card_number,
            'card_type':payment_method.card_type,'billing_address':payment_method.billing_address})

            # Update context
            context['card_number'] = '****-****-****-' + str(payment_method.card_number)[12:]
            context['card_type'] = payment_method.card_type

        except ValidationError as err:
            for err in err.messages:
                form.add_error(None, err)
            action = 'ERROR'
        except:
            print('Unexpected error: ' + str(sys.exc_info()[0]))
            action = 'ERROR'
    else:
        form = forms.EditPaymentForm(request.POST)

        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            # Extract form values
            card_number = form.cleaned_data['card_number']
            card_type = form.cleaned_data['card_type']
            billing_address = form.cleaned_data['billing_address']

            # Update context
            context['card_number'] = '****-****-****-' + str(card_number)[12:]
            context['card_type'] = card_type
            
            try:
                models.edit_process(id, int(card_number), card_type, billing_address)
                action = 'EDIT_SUCCESSFULL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'ERROR'
            except:
                print("Unexpected error: " + sys.exc_info()[0])
                form.add_error(None,'Unexpected error - Please contact your system administrator')
                action = 'ERROR'
        else:
            action = 'ERROR'

    return render(request, 'payment/edit_payment_form.html', {'action': action, 'context':context, 'form': form, 'title': title})
'''
'''
def delete_payment(request):

    id = request.POST.get('id','')
    if(id == ''):
        return HttpResponseRedirect('/payment/#mainsection')
    else: 
        id =id.replace('popup','')
    
    try:
        models.delete_process(id)
    except:
        print("Unexpected error: " + sys.exc_info()[0])
    
    return HttpResponseRedirect('/payment/#mainsection')
    '''