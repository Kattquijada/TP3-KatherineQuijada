from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"control/index.html")
def about(request):
    return render(request,"control/about.html")