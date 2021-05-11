from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('tajlake',views.tajlake,name='tajlake'),
]