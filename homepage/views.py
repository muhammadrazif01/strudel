from django.shortcuts import render

# Create your views here.

def homepage(request):
    response = {}
    return render(request, 'homepage.html', response)