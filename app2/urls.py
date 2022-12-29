from django.urls import path
from app2.views import*
app_name='nabj'

urlpatterns =[ 
    path('nan/',nan,name='nan')
]