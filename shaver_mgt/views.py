from django.shortcuts import render
from . import forms, models
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
import sys 

# Create your views here.


def add_shaver(request):
    title = "Add a new shaver"
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = forms.ShaverForm(request.POST)
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            # Extract form values
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            color = form.cleaned_data['color']
            type = forms.RAZORS[int(form.cleaned_data['type'])][1]
            qty = form.cleaned_data['qty']
            shave_image = form.cleaned_data['shave_image']

            try:
                models.create_process(brand, model, color, type, qty, shave_image)
                action = 'POST_SUCCESSFULL'
            except ValidationError as err:
                for err in err.messages:
                    form.add_error(None, err)
                action = 'POST_FAILED'
            except:
                print("Unexpected error: " + sys.exc_info()[0])
                form.add_error(None,'Unexpected error - Please contact your system administrator')
                action = 'POST_FAILED'
        else:
            action = 'POST_FAILED'
    else:
        action = 'GET'
        form = forms.ShaverForm(auto_id=False, initial={
                              'shave_image': 'http://'})
    return render(request, 'shaver/shaver_form.html', {'action': action, 'form': form, 'title': title})

def fetch_all_shavers(request):
    shaver_dict = models.fetch_all_shavers_process()
    
    return render(request, 'homepage.html', {'shaver_dict': shaver_dict})

def edit_shaver(request):
    id = request.POST.get('id','')

    # If id doesn't exist, redirect to the homepage
    if(id == ''):
        return HttpResponseRedirect('/')
    
    title = "Edit shaver"
    # Create an empty form so that Django doesn't complaint
    form = forms.ShaverForm()

    if('popup' in id):
        action = ''

        # Clean up the id
        id = id.replace('popup','')

        try:
            # Fetch the song from the DB based on the given id, and then populate the fields 
            shaver = models.fetch_shaver_process(id)
            form = forms.ShaverForm(auto_id=False, initial={'id':shaver.id,'brand':shaver.brand,
            'model':shaver.model,'type':forms.searchRazorsForKey(shaver.type),
            'color':shaver.color, 'qty':shaver.qty,'shave_image': shaver.shave_image})
        except ValidationError as err:
            for err in err.messages:
                form.add_error(None, err)
            action = 'ERROR'
        except:
            print('Unexpected error: ' + str(sys.exc_info()[0]))
            action = 'ERROR'
    else:
        form = forms.ShaverForm(request.POST)
        # Call is_valid() to validate data and create cleaned_data and errors dict
        if form.is_valid():
            # Extract form values
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            color = form.cleaned_data['color']
            type = forms.RAZORS[int(form.cleaned_data['type'])][1]
            qty = form.cleaned_data['qty']
            shave_image = form.cleaned_data['shave_image']

            try:
                models.edit_process(id, brand, model, color, type, qty, shave_image)
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

    return render(request, 'shaver/edit_shaver_form.html', {'action': action, 'form': form, 'title': title})

def delete_shaver(request):

    id = request.POST.get('id','')
    if(id ==''):
        return HttpResponseRedirect('/')
    else:
        id = id.replace('popup','')
    
    try: 
        models.delete_process(id)
    except:
        print("Unexpected error: " + sys.exc_info()[0])
    
    return HttpResponseRedirect('/')

    #redone 31 Oct