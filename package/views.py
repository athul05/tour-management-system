from django.shortcuts import render,redirect
from .models import Destination
from .forms import CheckoutForm
from django.contrib.auth.models import User,auth

# Create your views here.
def usr(request):
    dests = Destination.objects.all()
    return render(request, "usr-index.html", {'dests': dests})


def pkg_details(request):
    
    return render(request, "package-details.html")

def pkgs(request):
    dests = Destination.objects.all()
    return render(request, "packages.html",{'dests': dests})
    

def testim(request):
    return render(request, "testimonials.html")

def about(request):
    return render(request, "about.html")

def checkout(request):
    return render(request, "checkout.html")

def logout (request):
    auth.logout(request)
    return redirect('/')


    