# Option 1
from django.shortcuts import render
def help_version1(request):
    contact_info = {}
    """ Prepare contact_info data here """
    return render(request,'payment/help.html', contact_info)

# Option 2
from django.template.response import TemplateResponse
def help_version2(request):
    contact_info = {}
    """ Prepare contact_info data here """
    return TemplateResponse(request,'payment/help.html', contact_info)  

# Option 3
from django.http import HttpResponse
from django.template import loader, Context
def help_version3(request):
    contact_info = {}
    """ Prepare contact_info data here """
    response = HttpResponse()
    template = loader.get_template('payment/help.html')
    context = Context(contact_info)
    return response.write(template.render(context))



