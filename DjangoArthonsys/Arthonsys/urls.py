from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('Contacts/', views.contact, name="Contacts"),
]
