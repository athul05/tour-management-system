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
            messages.info(request, 'Thanks for creating account with us ! . Sign-In to your account to continue')
            return redirect('join')
    else:
        return render(request, "join.html")

def join(request):
    return render(request, "join.html")