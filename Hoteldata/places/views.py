from django.shortcuts import render

# Create your views here.

def tajlake(request):
    return render(request,'TAJ_MAD.html')

def udaipur(request):
    return render(request,'UDAIPUR.html')

def UMAID_BHAWAN_PALACE(request):
    return render(request,'UMAID_BHAWAN_PALACE.html')

def tajmahal(request):
    return render(request,'hotel1.html')

def chhatra(request):
    return render(request,'Hotel Chhatra Sagar.html')

def Glengurn(request):
    return render(request,'Hotel_Glengurn_tea_estate.html')

def soukya(request):
    return render(request,'Hotel Soukya.html')

def vivanta(request):
    return render(request,'Hotel Vivanta Dal View.html')

