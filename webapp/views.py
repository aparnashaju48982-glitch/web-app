from django.shortcuts import render, redirect 
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup_page.html')

def loginpage(request):
    return render(request, 'loginpage.html')

@login_required(login_url = 'loginpage')
def aboutpage(request):
    # if 'uid' in request.session:
    # if request.user.is_authenticated:
    return render(request, 'about.html')
    # else:
    #     return render(request, 'loginpage.html')

def usercreate(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!!')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
                user.save()

        else:
            messages.info(request, 'Password does not match!!')
            return redirect('signup')
        return redirect('loginpage')
    return render(request, 'signup_page.html')

def loginp(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            # request.session["uid"] = user.id
            if user.is_staff == 1:
                login(request,user)
                return redirect('adminhome')
            else:
                auth.login(request,user)
                messages.info(request, f'Welcome {username}')
                return redirect('aboutpage')
        else:
            messages.info(request, 'Invalid username or password!!')
            return redirect('loginpage')
    return render(request, "loginpage.html")

@login_required(login_url = 'loginpage.html')
def logout(request):
    # request.session["uid"] = user.id
    # if request.user.is_authenticated:
    auth.logout(request)
    return redirect('home')

def adminhome(request):
    return render(request, 'admin.html')