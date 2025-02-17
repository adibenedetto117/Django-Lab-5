from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

def hello_world_page(request):
    return render(request, 'myapp/helloworld.html')