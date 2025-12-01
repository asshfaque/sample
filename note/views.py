from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def intro(request):
    return render(request,"intro loading page.html")

def home(request):
    return render(request,"home.html")

