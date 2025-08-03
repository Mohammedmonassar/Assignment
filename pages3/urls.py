from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_pages3,name='view_pages3'),
    
]