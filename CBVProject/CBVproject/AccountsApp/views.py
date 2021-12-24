from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from .forms import UserCreationFormEmail
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

otp = None
user = None
def registerView(request):
    form = UserCreationFormEmail()
    if request.method == 'POST':
        form = UserCreationFormEmail(request.POST)
        if form.is_valid():
            global user
            username = request.POST['username']
            email = request.POST['email']
            form.save()
            user = User.objects.get(username=username)
            user.is_active = False                         # default value of is_active = True
            user.save()                                    # so we need to keep it false.
            global otp
            otp = random.randint(1000,9999)
            subject = 'verification otp'
            message = f'Hi {username}, thank you for registering in Python World.Your email verification OTP is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect("otp_verify")
    template_name = 'AccountsApp/register.html'
    context = {'form':form}
    return render(request, template_name, context)


def loginView(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        print(un)
        print(pw)
        user = authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            subject = 'welcome to Django world'
            message = f'Hi {user.username}, thank you for registering in CBVproject.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('show')
        else:
            messages.error(request,'Invalid Credentials !')
    context = {}
    template_name = 'AccountsApp/login.html'
    return render(request, template_name, context)

#def registrationView(request):
    #form = UserCreationForm()
    #if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('login')
    #context = {'form':form}
    #template_name = 'AccountsApp/register.html'
    #return render(request, template_name, context)



def logoutView(request):
    logout(request)
    return redirect('login')

def otpVerifyView(request):
    if request.method == 'POST':
        num = request.POST.get('otp')
        if int(num) == otp:
            user.is_active = True
            user.save()
            return redirect("login")
        else:
            messages.error(request,"Invalid otp")
    template_name = 'AccountsApp/otpverify.html'
    context = {}
    return render(request, template_name, context)