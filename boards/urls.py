'''
    This file is used to define the URL patterns for the boards app.
'''

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.boards, name='boards'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
