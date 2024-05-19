'''
    This file is used to render the fanart page.
'''

from django.shortcuts import render

# Create your views here.
def fanart(request):
    ''' Render the shopping cart page '''
    return render(request, 'fanart/fanart.html')
