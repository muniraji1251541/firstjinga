from django.shortcuts import render

# Create your views here.

def second(request):
    d={'name':'Muniraji','age':22,'gender':'Male','mail':'muniraji1251541@gmail.com','mobile':8754685230}
    return render(request,'second.html',context=d)