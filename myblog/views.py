from django.shortcuts import render

def index(request):
    return render (request,"myblog/index.html")

def blogs(request):
    return render (request,"myblog/blogs.html")

def contact(request):
    return render (request,"myblog/contact.html")