from django.shortcuts import render

# Create your views here.

def index(request):
    # this is the new views
    return render(request, 'index.html')
