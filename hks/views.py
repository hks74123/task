
import email
from django.shortcuts import render
from django.core.checks import messages
import datetime
from datetime import timezone
from hks.models import User1, profile_details 
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render,HttpResponse

def home(request):
    if request.user.is_authenticated:
        get_prof=profile_details.objects.filter(user=request.user)
        return render(request,'done.html',{"prof":get_prof})
    else:
        return render(request,'home.html') 

def docsign(request):
    if request.user.is_authenticated:
         return render(request,'dashboard.html')
    else:
        user='Doctor'
        hks=0
        return render(request,'login.html',{'type':user,'hks':hks})

def patsign(request):
    if request.user.is_authenticated:
         return render(request,'dashboard.html')
    else:
        user='Patient'
        hks=0
        return render(request,'login.html',{'type':user,'hks':hks})
    
def register(request,pid):
    if request.method=='POST':
        first_name=request.POST.get('f_name')
        second_name=request.POST.get('l_name')
        username=request.POST.get('u_name')
        mail=request.POST.get('mmail')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        state=request.POST.get('state')
        city=request.POST.get('city')
        passw=request.POST.get('pass')
        passw1=request.POST.get('pass1')

        if(first_name=='' or second_name=='' or username=='' or mail=='' or address=='' or pincode=='' or state=='None' or city=='None' or passw=='' or passw1=='' or len(request.FILES)==0):
            messages.error(request,'Please fill out all the fields and upload a profile pic !!')
            user22=pid
            hks=0
            return render(request,'login.html',{'type':user22,'hks':hks})
        if(len(pincode)!=6):
            messages.error(request,'Invalid Pincode')
            user22=pid
            hks=0
            return render(request,'login.html',{'type':user22,'hks':hks}) 
        if passw==passw1:
            if User1.objects.filter(username=username).exists():
                messages.error(request,'Username already exists!!')
                user22=pid
                hks=0
                return render(request,'login.html',{'type':user22,'hks':hks})
            elif User1.objects.filter(email=mail).exists():
                messages.error(request,'Email already exists!!')
                user22=pid
                hks=0
                return render(request,'login.html',{'type':user22,'hks':hks})
            else:
                if(pid=='Doctor'):
                    pos=User1.objects.create(username=username,password=passw,email=mail,first_name=first_name,last_name=second_name,is_Doctor=True)
                    pos.save()
                else:
                   pos=User1.objects.create(username=username,password=passw,email=mail,first_name=first_name,last_name=second_name,is_Patient=True)
                   pos.save()
                prof=profile_details(user=pos,imgp=request.FILES['imgle'],u_nm=username,fstname=first_name,secname=second_name,terimail=mail,timestamp=datetime.datetime.now(timezone.utc),address1=address,pincode=pincode,state=state,city=city)
                prof.save()
                user22=pid
                hks=1
                messages.info(request,'Signup Success now you can login ')
                return render(request,'login.html',{'type':user22,'hks':hks})
        else:
            user22=pid
            hks=0
            messages.error(request,'Password did not matched !!')
            return render(request,'login.html',{'type':user22,'hks':hks})


def login(request,pid):
    if request.method=='POST':
        username=request.POST.get('ul_name')
        passw=request.POST.get('lpass')

        if(username=='' or passw==''):
            user22=pid
            hks=1
            messages.error(request,'Please enter all the fields')
            return render(request,'login.html',{'type':user22,'hks':hks})
        else:
            get_user=User1.objects.get(username=username,password=passw)
            print(get_user.is_Doctor)
            if get_user is not None:
                if(pid=='Doctor'):
                    if(get_user.is_Doctor==True):
                        auth.login(request,get_user)
                        get_prof=profile_details.objects.get(user=get_user)
                        return redirect('/')
                    else:
                        messages.error(request,'You have a patient accoutn so login into patients portal')
                        user22=pid
                        hks=1
                        return render(request,'login.html',{'type':user22,'hks':hks}) 
                else:
                    if(get_user.is_Doctor==True):
                        messages.error(request,'You have a Doctor accout so login into Docotrs portal')
                        user22=pid
                        hks=1
                        return render(request,'login.html',{'type':user22,'hks':hks})
                    else:
                        auth.login(request,get_user)
                        get_prof=profile_details.objects.get(user=get_user)
                        return redirect('/')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/')
    else:
        user='Doctor'
        hks=0
        return render(request,'login.html',{'type':user,'hks':hks})