from django.shortcuts import render,redirect
from .models import Destination,Testimonial,Blog,Booking
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
    if request.method == 'POST':
        dest=Destination.objects.filter(id=oid).first()
        form = CheckoutForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            place = dest.name
            name = form.cleaned_data.get('name')
            number = form.cleaned_data.get('number')
            package= form.cleaned_data.get('package')
            date= form.cleaned_data.get('date')
            if package == 'Car':
                package_prize= dest.car
            elif package == 'Mini-Van':
                package_prize = dest.van
            elif package == 'Traveller':
                package_prize = dest.trav
            else:
                package_prize = dest.bus
            
            book= Booking(
                name=name,
                number=number,
                package=package,
                date=date,
                place=place,
                package_prize=package_prize
            )
            book.save()
            return render(request, "checkout.html", {'dest':dest, 'form':form})
        else:
            return render(request, "checkout.html", {'dest':dest, 'form':form})
            
    else:
        form= CheckoutForm()
        dest=Destination.objects.filter(id=oid).first()
        return render(request, "checkout.html", {'dest':dest, 'form':form})

def logout (request):
    auth.logout(request)
    return redirect('/')


    