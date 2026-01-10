from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def service(request):
    return render(request, 'service.html')

def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')