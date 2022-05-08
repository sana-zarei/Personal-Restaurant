from audioop import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .forms import UserLoginForm, ProfileRegisterForm
from Restaurant.models import Profile,Contact
from django.contrib.auth.views import PasswordResetDoneView



def loginview(request):

    contact = Contact.objects.latest('updated')
    profile = Profile.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('Restaurant:home'))
        else:
            context = {"username":username, "ErrorMessage":": Username or Password Error","profile":profile, "form":UserLoginForm}
            return render(request, 'login.html',context)
    else:
        return render(request, 'Accounts/login.html',{"form":UserLoginForm,"profile":profile,'contact':contact})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('Restaurant:home'))



def registerview(request):

    contact = Contact.objects.latest('updated')
    profile = Profile.objects.all()

    if request.method=="POST":
        profileregisterform=ProfileRegisterForm(request.POST or None)
        if profileregisterform.is_valid():
            user = User.objects.create_user(username=profileregisterform.cleaned_data["username"],email=profileregisterform.cleaned_data['email'],password=profileregisterform.cleaned_data['password'])
            user.save()
            return JsonResponse({'msg':'Success'})
            # return HttpResponseRedirect(reverse('Accounts:login'))
        else:
            return JsonResponse({'msg':'Error'})
    else:
        profileregisterform=ProfileRegisterForm()

    return render(request, 'Accounts/register.html',{"form":profileregisterform,"profile":profile,'contact':contact})

