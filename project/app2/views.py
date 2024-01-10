from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django import template
from .models import cars
from django.db.models import Q
from .forms import *

# def car_search(request):
#     print("in")
#     if request.method == 'POST':
#         query = request.POST.get('query')
#         print(query)
#         if query:
#             cars = cars.objects.filter(name__icontains = query)
#             if cars:
#                 search_history = request.session.get('search_history', [])
#                 search_history.insert(0, query)
#                 request.session['search_history'] = search_history[:5]
                
#                 return render(request, 'search_results.html', {'cars': cars})
#             else:
#                 messages.warning(request, 'No cars found with that name.')
                
#     return render(request, 'car_search.html')

def HomePage(request):
    cares = cars.objects.all()
    # filter_form = ItemFilterForm(request.GET)
    # if filter_form.is_valid():
    #     name = filter_form.cleaned_data.get('name')
    #     price = filter_form.cleaned_data.get('price')
    #     if name:
    #         car = car.filter(name__icontains=name)
    #     if price:
    #         car = car.filter(price=price)

    # context = {
    #     'car': car,
    #     'filter_form': filter_form
    # }
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            car = cars.objects.filter(name__icontains = query)
            if car:
                search_history = request.session.get('search_history', [])
                search_history.insert(0, query)
                request.session['search_history'] = search_history[:5]
                
                return render(request, 'car_search.html', {'cars': car})
            else:
                messages.warning(request, 'No cars found with that name.')     
        return render(request, 'car_search.html')
    

    return render(request, 'home.html', {'car': cares})

def detail_page(request, id):
    obj = get_object_or_404(cars, id = id)

    # if request.user.is_authenticated:
    #     max_viewed_books_length = 10
    #     viewed_books = request.session.get('viewed_books', [])
    #     viewed_book = [cars.id, cars.name]
    #     if viewed_book in viewed_books:
    #         viewed_books.pop(viewed_books.index(viewed_book))
    #     viewed_books.insert(0, viewed_book)
    #     viewed_books = viewed_books[:max_viewed_books_length]
    #     request.session['viewed_books'] = viewed_books

    return render(request, 'detail.html', {'obj' : obj}) 


def get(request, id):
    car = get_object_or_404(cars, pk=id)
    viewed_cars = request.session.get('viewed_cars', [])
    if id not in viewed_cars:
        viewed_cars.insert(0, id)
    request.session['viewed_cars'] = viewed_cars
    # print(viewed_cars)
    return render(request, 'detail.html', {'car': car})


register = template.Library()
@register.simple_tag(takes_context=True)
@login_required
def profile(request, count = 5):
    viewed_cars = request.session.get('viewed_cars', [])
    search = request.session.get('search_history', [])
    last_viewed_cars = []
    for car_id in viewed_cars[:count]:
        car = get_object_or_404(cars, pk=car_id)
        last_viewed_cars.append(car)
    return render(request, 'profile.html', {'last_viewed_cars': last_viewed_cars, 'search_history': search})

def SignupPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
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

        
        print(name, generation, body, EngCap, transmission, drive, price, customs_cleared, rudder, run, image, colour, description, city, number)
     
        car = cars.objects.create(name = name, generation = generation, body = body, EngCap = EngCap, transmission = transmission, drive = drive, price = price, customs_cleared = customs_cleared, rudder = rudder, run = run, image = image, colour = colour, description = description, city = city, number = number)
        car.save()

    return render(request, 'add.html')


def adminPage(request):
    cus = Customer.objects.all()
    contex = {'cus': cus}
    return render(request, 'admin.html', contex)


def profAdmin(request):
    prof = Profile.objects.all()
    contex = {'prof': prof}
    return render(request, 'profileAdm.html', contex)


def profEdit(request):
    prof = Profile.objects.all()
    context = {
        'prof': prof,
    }
    return render(request, 'profileAdm.html')


def updateProf(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        phone = request.POST.get('phone')
        descript = request.POST.get('descript')

        prof = Profile(
            id=id,
            name=name,
            title=title,
            phone=phone,
            descript=descript
        )
        prof.save()
        return redirect('profAdmin')
    return redirect(request, 'profileAdmin.html')


def deleteProf(request, id):
    prof = Profile.objects.filter(id=id)
    prof.delete()
    contex = {
        'prof': prof,
    }
    return redirect('profAdmin')


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        cus = Customer(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        cus.save()
        return redirect('adminPage')
    return render(request, 'admin.html')


def edit(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
    }
    return redirect(request, 'admin.html', context)


def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        cus = Customer(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        cus.save()
        return redirect('adminPage')
    return redirect(request, 'admin.html')


def delete(request, id):
    cus = Customer.objects.filter(id=id)
    cus.delete()
    contex = {
        'cus': cus,
    }
    return redirect('adminPage')


def filterPrice(request):
    products = cars.objects.all()
    if request.method == "POST":
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        if min_price and max_price:
            products = products.filter(prices__range=(float(min_price), float(max_price)))
        elif min_price:
            products = products.filter(prices__gte=float(min_price))
        elif max_price:
            products = products.filter(prices__lte=float(max_price))
    context = {'products': products}
    return render(request, 'filter.html', context)


# @login_required(login_url='login')
# def profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             username = request.user.username
#             messages.success(request, f'{username},Your profile is update.')
#             return redirect('/')
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     contex = {'form': form}
#     return render(request, 'profile.html', contex)

# Create your views here.
