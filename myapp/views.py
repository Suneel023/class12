from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def motto(request):
    return HttpResponse("<h1>Project is ready to launch</h1>")

def main(request):
    return render(request,"main.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Superman Man of Steel"
    return render(request,"myapp/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    email=request.GET.get('email')
    return render(request,"get_demo.html",{'name':name,'email':email})

def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        return HttpResponse("<h4>Thanks for submission Mr./Ms. {} with your email-address {}</h4>".format(name,email))
    return render(request,"post_demo.html")