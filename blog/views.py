from django.shortcuts import render # noqa
from django.http import HttpResponse


# Create your views here.
def my_blog(request):
    return HttpResponse("Starting well...")
