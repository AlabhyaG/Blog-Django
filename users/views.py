from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from . forms import *
from django.contrib import messages
from django.contrib.auth.models import User

def loginView(request):
    f=LoginForm(request.POST)
    if request.method=='POST':
        f=LoginForm(request.POST) 
        if(f.is_valid()==True):
            username=f.cleaned_data['username']
            password=f.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Login Successful')
                return redirect('Home')
            else:
                messages.error(request,"User does not exits, either return to home page or login again")    
                return redirect('login')
        else:
            messages.error(request,"You have enterd invalid details")
            return redirect('login')    
    context={      
        'form':f
    }        
    return render(request,'login.html',context)

def logoutView(request):
    if request.method=="POST":
        logout(request)
        return redirect('Home')
    return render(request,'logout.html',{})

def registerView(request):
    userForm=UserRegistrationForm(request.POST or None)
    profileForm=ProfileRegistrationForm(request.POST or None)
    if request.method=='POST':
        if userForm.is_valid() and profileForm.is_valid():
            username=userForm.cleaned_data.get('username')
            first_name=userForm.cleaned_data.get('first_name')
            last_name=userForm.cleaned_data.get('last_name')
            email=userForm.cleaned_data.get('email')
            gender=profileForm.cleaned_data.get('gender')
            password=userForm.cleaned_data.get('password')
            confirm_passoword=userForm.cleaned_data.get('confirm_password')
            if password!=confirm_passoword:
                #password not match
                # need to populate the form this time
                return render(request,'register.html',{})
            else :
                user=userForm.save(commit=False)
                user.set_password(password)
                user.save()
                profile=profileForm.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('login')
    return render(request,'register.html',{'userForm':userForm,'profileForm':profileForm})

def profileView(request,pk):
    user=get_object_or_404(User,id=pk)
    profile=get_object_or_404(Profile,user=user)
    context={
        'profile':profile,
        'u':user
    }
    return render(request,'user_profile.html',context)

def profileUpdateView(request,pk):
    user=get_object_or_404(User,id=pk)
    profile=get_object_or_404(Profile,user=user)
    initial_data={
       'first_name':user.first_name,
       'last_name':user.last_name,
       'email':user.email,
       'username':user.username,
       'gender':profile.gender

    }
    if request.method=="POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            profile.gender = form.cleaned_data['gender']
            user.save()
            profile.save()
            return redirect('profile', pk=pk)
    else:
        form=UserUpdateForm(initial=initial_data)    
    context={'form':form}
    return render(request,'update_profile.html',context)    


