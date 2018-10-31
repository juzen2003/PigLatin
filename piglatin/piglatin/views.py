from django.http import HttpResponse
#  this is for showing html as response
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
# def hello(request):
#     return HttpResponse("Hello World!")
def translate(request):
    # request.GET['originaltext'] -> originaltext inputed from form is passed to translate page from request
    return HttpResponse("You are at the translate page!" + request.GET['originaltext'])
