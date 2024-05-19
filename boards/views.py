'''
This file is used to render the message boards page.
'''

from django.shortcuts import render

# Create your views here.
def boards(request):
    ''' Render the boards page '''

    return render(request, 'boards/boards.html')
