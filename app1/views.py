from django.shortcuts import render

# Create your views here.

def first(request):
    d={'Username':'Logan','Age':20}
    return render(request,'first.html',context=d)