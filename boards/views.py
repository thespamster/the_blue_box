from django.shortcuts import render

# Create your views here.
def boards(request):
    ''' Render the shopping cart page '''

    return render(request, 'boards/boards.html')
