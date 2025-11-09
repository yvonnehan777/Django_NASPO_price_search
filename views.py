from django.http import HttpResponse
from django.shortcuts import render

def search(request):
    return render(request, 'catalog_app/search.html')

def health(request):
    return HttpResponse("OK")
