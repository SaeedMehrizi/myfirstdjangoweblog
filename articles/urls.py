from .views import *
from django.urls import path, include


urlpatterns = [

    path('', articles_list),
]
