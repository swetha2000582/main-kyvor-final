from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('instruclogin',views.instruclogin,name='instruclogin'),
    path('forms',views.forms,name='forms'),
    path('instructreg',views.instructreg,name='instructreg'),
    path('show/<int:id>',views.show,name='show'),
]