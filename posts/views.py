from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def hello_world(request) :
    if request.method == "GET":
        return JsonResponse({
            'status': 200,
            'data': "Hello likelion-12th!"
        })
    
def index(request):
    return render(request, 'index.html')
    
