from django.urls import path
from . import views
urlpatterns = [
    path('tajlake',views.tajlake,name='tajlake'),
    path('udaipur',views.udaipur,name='udaipur'),
    path('UMAID_BHAWAN_PALACE',views.UMAID_BHAWAN_PALACE,name='UMAID_BHAWAN_PALACE'),
    path('tajmahal',views.tajmahal,name='tajmahal'),
    path('chhatra',views.chhatra,name='chhatra'),
    path('Glengurn',views.Glengurn,name='Glengurn'),
    path('soukya',views.soukya,name='soukya'),
    path('vivanta',views.vivanta,name='vivanta'),
]