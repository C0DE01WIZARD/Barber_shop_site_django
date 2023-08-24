from django.urls import path
from hair.views import *

urlpatterns = [
    path('news/', news, name='news'),
    path('records/',records, name='record')


]