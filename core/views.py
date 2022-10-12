from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.
def index(request,id):
    return render(request,'index.html',{"id":id})