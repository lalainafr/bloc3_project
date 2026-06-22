from django.shortcuts import render

def home(request):
    return render (request, 'bloc3_app/home.html')
