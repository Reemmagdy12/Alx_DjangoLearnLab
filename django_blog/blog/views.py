from django.shortcuts import render, redirect
from .forms import SignUPForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
@login_required
def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST' :
        form = SignUPForm(request.POST)
        if form.is_valid :
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            redirect('home')
    else :
        context = {
            form : SignUPForm
        }
        return render (request, 'registration/register.html',context)
    
@login_required
def profile(request):
    if request.method == 'POST' :
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        redirect('profile')
    else:
        return render (request,'profile.html',{'user':request.user})


