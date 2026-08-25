from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    people = [{'name':'abhijeet', 'age':20}, {'name':'krushna', 'age':28}, {'name':'sarvjeet', 'age':24}, {'name':'abhishek', 'age':30}, {'name':'shubham', 'age':17}]
    return render(request, "a.html", context={'people' : people})

def success_page(request):
    return render(request, "index.html")