from django.shortcuts import render,redirect
from .models import Destination,Testimonial,Blog
from .forms import CheckoutForm
from django.contrib.auth.models import User,auth

# Create your views here.


def usr(request):
    tests = Testimonial.objects.all()
    dests = Destination.objects.all()
    blogs = Blog.objects.all() 
    return render(request, "usr-index.html", {'dests': dests, 'tests':tests, 'blogs':blogs})


def pkg_details(request, oid ):
    dest=Destination.objects.filter(id=oid).first()
    return render(request, "package-details.html", {'dest': dest})

def pkgs(request):
    dests = Destination.objects.all()
    return render(request, "packages.html",{'dests': dests})
    

def testim(request):
    return render(request, "testimonials.html")

def about(request):
    return render(request, "about.html")

def checkout(request, oid):
    dest=Destination.objects.filter(id=oid).first()
    return render(request, "checkout.html", {'dest':dest})

def logout (request):
    auth.logout(request)
    return redirect('/')


    