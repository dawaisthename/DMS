from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User, auth,Group
from .models import Profile


def signup(request, *args,**kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request,"username Taken")
                return redirect('signup')
            else:
                user =User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                # user_login=auth.authenticate(username=username, password=password1)
                # auth.login(request,user_login)    
                user_model=User.objects.get(username=username)
                g = Group.objects.get(name='employee')
                g.user_set.add(user_model)

                return redirect('signin')

    return render(request, 'users/sign up.html')
def login(request, *args,**kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return render(request, 'users/sign in.html')

    else:     
        return render(request, 'users/sign in.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def logout(request, *args,**kwargs):
    auth.logout(request)
    return redirect('signin')