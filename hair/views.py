from django.shortcuts import render
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from hair.models import *
from hair.serializers import HairsSerializers


def news(request):  # request
    return render(request, 'news.html')  # response


def records(request):
    return render(request, 'record.html')

def index_page(request):  # request
    all_hairs = Barber.objects.all()  # получаем записи из таблицы
    return render(request, 'index.html', {'data': all_hairs})  # response


class Index_View(ModelViewSet):
    queryset = Hairstyles.objects.all()
    serializer_class = HairsSerializers
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['price']


def index_app(request):  # request
    return render(request, 'main_app.html')  # response


