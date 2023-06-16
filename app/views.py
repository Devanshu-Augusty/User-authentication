from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from app.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    username = request.user.username
    user_profile = Profile.objects.get(username = username)
    context = {'user_profile': user_profile}

    return render(request, "index.html", context)


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user')
        profile_pic = request.FILES.get('profile_pic')
        email = request.POST.get('email')
        type = request.POST.get('type')
        password = request.POST.get('pass')
        c_pass = request.POST.get('c_pass')
        house_number = request.POST.get('house_number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')

        address = str(house_number) + ", " + city + ", " + state + ", " + str(pin_code)

        if password != c_pass:
            messages.info(request, "Password and Confirmed password is not matching")
            return redirect('signup')

        user_profile = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user_profile.save()

        profile_model = Profile.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, profile_pic=profile_pic, address=address, type=type)
        profile_model.save()

        return redirect('login')
        

    return render(request, "signup.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')

        user = auth.authenticate(request, username=username, password=password)
        
        if user is None:
            messages.info(request, 'Wrong username or password')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('home')
        

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')