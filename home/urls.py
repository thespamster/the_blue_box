'''
    This file is used to define the URL patterns for the home app.
'''

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'home_page'

urlpatterns = [
    path('', views.index, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
