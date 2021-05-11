from django.urls import path,include
from . import views
urlpatterns = [
    path('visit',views.visit,name='visit'),
    # path('tajlake',views.tajlake,name='tajlake'),
    
]