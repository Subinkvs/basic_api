from django.urls import path
from .views import drink_list, drink_list_create, drinks_detail_view

urlpatterns =[
    path('drinks/', drink_list),
    path('drinks/create/', drink_list_create),
    path('drinks/<int:id>', drinks_detail_view)
]