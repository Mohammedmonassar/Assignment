from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_pages2,name='view_pages2'),
    
]