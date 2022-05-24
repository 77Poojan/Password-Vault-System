from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from api.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from api.models import UserVault
from api.utils import decrypt, encrypt
#from api.tasks import send_mail_task

#User Signup
def sign_up(request):
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                uemail = fm.cleaned_data['email']
                encryptedpassword = encrypt(fm.cleaned_data['password1'] )
                upass = encryptedpassword
                data = UserVault.objects.create(name=uname, email=uemail, password=upass)
                data.save()
                fm.save()
                messages.success(request,'Sucessfully Submitted')
        else:
            fm = SignUpForm()
        return render(request,'signup.html',{'form':fm})
    
#User Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
                fm = AuthenticationForm(request=request, data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    upass = fm.cleaned_data['password']               

                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request,user)
                        return HttpResponseRedirect('/userprofile/')
        else:
            fm=AuthenticationForm()
        return render(request,'userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userprofile/')

#User Profile
def user_profile(request):
    if request.user.is_authenticated:
        data = UserVault.objects.all()
        for record in data:
            record.password = decrypt(record.password)
        return render(request,'profile.html', {'data': data})
    else:
        return HttpResponseRedirect('/userlogin/')

#User Logout   
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/userlogin/')

#Change password using old password
def user_changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():         
                fm.save()
                upass = request.POST.get('new_password1')
                data = UserVault.objects.get(name=request.user, password=request.POST.get('old_password'))
                data.password = encrypt(upass)
                data.save() 
                update_session_auth_hash(request,fm.user)   
                messages.success(request,"Password Changed Sucessfully")
                return HttpResponseRedirect('/userprofile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userprofile/')


    