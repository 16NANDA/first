from django.urls import path
from app1.views import*
app_name="nanda"

urlpatterns = [ 
    path('first/',first,name='first'),
]