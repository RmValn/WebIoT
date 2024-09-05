from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model, login, logout, authenticate
from .forms import LoginForm, SignUpForm
# Create your views here.

def SignIn(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("fail")
    else:
        form = LoginForm()
    return render(request,"auth/signin.html", {'form': form})
    

def SignUp(request):
    if request.user.is_authenticated:
        return redirect("home")
    User = get_user_model()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, dob=dob, gender=gender)
            user = authenticate(username=username, password=password)
            if user is not None:
                print('kurwa')
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def SignOut(request):
    logout(request)
    return redirect('home')

def Home(request):
    return render(request=request, template_name="home.html")