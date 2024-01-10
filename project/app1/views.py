from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import cars

from .models import cars
@login_required(login_url = 'login')
def HomePage(request):
    obj = cars.objects.all()
    
    return render(request, 'home.html', {'obj' : obj})

def detail_page(request, id):
    obj = get_object_or_404(cars, pk = id)
    return render(request, 'detail.html', {'obj' : obj})

# @login_required(login_url = 'login')
# class HomePage(ListView):
#     context_object_name = 'obj'
#     template_name = 'home.html'
#     model = cars


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and comform password are not same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    
        print(uname, email, pass1, pass2)


    return render(request, 'signup.html')

def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user = authenticate(request, username = username, password = pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'User does not exist'
            return render(request, "login.html")
            

    return render(request, 'login.html' )

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Add_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        generation = request.POST.get('generation')
        body = request.POST.get('body')
        EngCap = request.POST.get('EngCap')
        transmission = request.POST.get('transmission')
        drive = request.POST.get('drive')

        price = request.POST.get('price')

        customs_cleared = request.POST.get('customs_cleared')
        rudder = request.POST.get('rudder')
        run = request.POST.get('run')

        image = request.POST.get('image')

        colour = request.POST.get('colour')

        description = request.POST.get('description')

        city = request.POST.get('city')
        number = request.POST.get('number')

        car = cars.object.create_cars(name, generation, body, EngCap, transmission, drive, price, customs_cleared, rudder, run, image, colour, description, city, number)
        car.save()

        print(name, generation, body, EngCap, transmission, drive, price, customs_cleared, rudder, run, image, colour, description, city, number)
     
    return render(request, 'add.html')


# Create your views here.
