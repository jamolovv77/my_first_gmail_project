from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from random import randint
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def registraion(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )
        user.save()
        
        code = str(randint(100000, 999999))
        EmailConfirm.objects.update_or_create(
            user = user,
            code = code
        )
        send_mail(
            "Confirm your email",
            f"Your code {code}",
            'norep1y@softc1ub.tj',
            [user.email]
        )
        return redirect('confirm_email')


    return render(request, "registration.html")



def home(request):
    return render(request, 'home.html')


def confirm_email(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        code = request.POST.get("code")
        user = User.objects.filter(username = username).first()
        code_obj = EmailConfirm.objects.filter(user = user).first()
        
        if code_obj.code == code:
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('profile')
        else:
            return redirect("confirm_email")
    return render(request, 'confirm_email.html')
    
    

    
        
@login_required        
def show_profile(request):
    return render(request, "profile.html")


        
        
        
    
        

        
        
        

def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username = data['username'], password = data['password'])
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return redirect("login")
    return render(request, 'login.html')




def send_oll_mesage_for_our(request):
    users = User.objects.filter(is_active=True)

    for user in users:
        send_mail(
            "salom","salom, ruz baxayr !",
            None,[user.email],
            fail_silently=False
        )

    return redirect('profile')



def home(request):
    user = User.objects.all()
    return render(request,'home.html', {'user':user})
