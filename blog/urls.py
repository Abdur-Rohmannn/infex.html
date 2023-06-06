from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    #path('categ/<int:pageid>/', cats, name='cats')
]