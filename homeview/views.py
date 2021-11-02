from django.shortcuts import render

# Create your views here.

def Homeview(request):
    return render(request, 'homepage/index.html')

def Catview(request):
    return render(request, 'homepage/cat.html')

def Dogview(request):
    return render(request, 'homepage/dog.html')
