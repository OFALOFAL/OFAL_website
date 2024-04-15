from django.shortcuts import render


def home(request):
    return render(request, 'webApp/home.html')


def GDD(request):
    return render(request, 'webApp/GDD.html')
