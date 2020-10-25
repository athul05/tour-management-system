from django.shortcuts import render,redirect
from .models import Destination,Testimonial,Blog,Booking,Enquirie,Feedback
from .forms import CheckoutForm,Enquiry,Feed
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.


def usr(request):
    feed = Feed()
    tests = Testimonial.objects.all()
    dests = Destination.objects.all()
    blogs = Blog.objects.all() 
    return render(request, "usr-index.html", {'dests': dests, 'tests':tests, 'blogs':blogs, 'feed':feed})


def pkg_details(request, oid ):
    form = Enquiry()
    dest=Destination.objects.filter(id=oid).first()
    return render(request, "package-details.html", {'dest': dest, 'form':form})

def pkgs(request):
    dests = Destination.objects.all()
    return render(request, "packages.html",{'dests': dests})
    

def testim(request):
    return render(request, "testimonials.html")

def about(request):
    return render(request, "usr-about.html")

def checkout(request, oid):
    if request.method == 'POST':
        dest=Destination.objects.filter(id=oid).first()
        form = CheckoutForm(request.POST)
        if form.is_valid():
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
            username= request.user
            book= Booking(
                username=username,
                name=name,
                number=number,
                package=package,
                date=date,
                place=place,
                package_prize=package_prize
            )
            book.save()

            return render(request, "success.html", {'dest':dest, 'book':book})
        else:
            return render(request, "checkout.html", {'dest':dest, 'form':form})
            
    else:
        form= CheckoutForm()
        dest=Destination.objects.filter(id=oid).first()
        return render(request, "checkout.html", {'dest':dest, 'form':form})

def logout (request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, "usr-contact.html")
def index(request):
    return redirect("usr")
    
def sucess(request):
    return redirect("usr")

def enquiry(request, oid):
    if request.method == 'POST':
        form=Enquiry(request.POST)
        dest=Destination.objects.filter(id=oid).first()
        if form.is_valid():
            name = form.cleaned_data.get('name')
            number = form.cleaned_data.get('number')
            message = form.cleaned_data.get('message')
            package = dest.name
            username= request.user
            urgent= request.POST.get('urgent',"No");
            enq = Enquirie(
                username= username,
                name = name,
                number= number,
                message= message,
                urgent=urgent,
                package = package
            )
            enq.save()
            messages.success(request, 'Your enquiry has been succefully submitted !')
            return redirect('index')

        else:
            form = Enquiry()
            dest=Destination.objects.filter(id=oid).first()
            return render(request, "package-details.html", {'dest': dest, 'form':form})

def feedback(request):
    if request.method == 'POST':
        feed=Feed(request.POST)
        if feed.is_valid():
            name = feed.cleaned_data.get('name')
            email = feed.cleaned_data.get('email')
            subject = feed.cleaned_data.get('subject')
            message = feed.cleaned_data.get('message')
            rating = feed.cleaned_data.get('rating')
            username = request.user
            feedbck = Feedback(
                username=username,
                name = name,
                email= email,
                subject= subject,
                message = message,
                rating=rating
            )
            feedbck.save()
            messages.success(request, 'Thanks for your feedback fellow traveller !')
            return redirect('index')

        else:
            return redirect('index')
    
def order_history(request):
    uname=request.user
    books=Booking.objects.filter(username=uname).all()

    return render(request,'order_history.html',{'books':books})