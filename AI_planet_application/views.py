from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import HackathonForm,RegistrationForm

# Create your views here.


@login_required(login_url="login")
def home(request):
    context={}
    return render(request,'home.html',context)



@login_required(login_url="login")
def hackathon(request,hackathon_id):
    context = {
        "hackathon_id":hackathon_id
    }
    return render(request,'hackathon.html',context)

@login_required(login_url="login")
def hackathonSubmit(request,hackathon_id):
    context = {
        "hackathon_id":hackathon_id
    }
    return render(request,'submit.html',context)


def createHackathon(request):
    
    context={
        'form':HackathonForm()
    }
    return render(request,'form.html',context)



def login_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    
    if request.method=='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'username or password incorrect')
    context={}
    return render(request,'login.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "GET":
        registrationForm = RegistrationForm()
        context={
            'form':registrationForm
        }
        return render(request,'register.html',context)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST.get('username').lower()
            password = request.POST.get('password1')

            try:
                user=User.objects.get(username=username)
            except:
                messages.error(request,'User does not exist')
            
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
        
    return render(request,'register.html',{'form':RegistrationForm()})


def my_hackathons(request,hackathon_id):
    return render(request,'my_hackathons.html',{'hackathon_id':hackathon_id})