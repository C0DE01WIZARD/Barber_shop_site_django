from django.urls import path
from hair.views import news

urlpatterns = [
    path('news/', news)

]