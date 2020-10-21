from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render (request,"index.html")

def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        username= request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Oops!. Username Already exist. Try again with a different username')
            return redirect('join')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Oops!.Email Already exist. Try again with a different email')
            return redirect('join')
        else:
            user =User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
            user.save()
            return render(request,"thanks.html")

    else:
        return render(request, "join.html")

def join(request):
    return render(request, "join.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect ("usr")
        else:
            messages.info(request, 'Oops!.Incorrect Credentials. Try again')
            return redirect('join')
    else:
        return redirect('join')
            

def signin(request):
    return redirect('join')

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def abcontact(request):
    return redirect('/')
