from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Listing

# Home page view
def home(request):
    return render(request, 'index.html')

# Admin Login View
def admin_login(request):
    error_message = None  # Initialize error message variable
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('add_vehicle')  # Redirect to the add_vehicle page after successful admin login
        else:
            error_message = "Invalid username or password"  # Set error message

    return render(request, 'admin_login.html', {'error_message': error_message})

# Admin Logout View
def admin_logout(request):
    logout(request)
    return redirect('home')

# Add Vehicle View (restricted to admins)
@login_required
def add_vehicle(request):
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        brand = request.POST.get('brand')
        mileage = request.POST.get('mileage')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Create a new Listing object in the database
        Listing.objects.create(
            name=name,
            description=description,
            brand=brand,
            mileage=mileage,
            price=price,
            image=image
        )
        return redirect('listings')  # Redirect to the listings page after adding

    return render(request, 'add_vehicle.html')

# Vehicles page view (currently static list)
def vehicles(request):
    vehicles = [
        {"image": "vehicle4.jpg"},
        {"image": "vehicle15.jpeg"},
        {"image": "vehicle49.jpeg"},
        {"image": "vehicle45.jpeg"},
        {"image": "vehicle5.jpg"},
        {"image": "vehicle6.jpg"},
        {"image": "vehicle7.jpg"},
        {"image": "vehicle8.jpg"},
        {"image": "vehicle9.jpg"},
        {"image": "vehicle10.jpg"},
        {"image": "vehicle11.jpg"},
        {"image": "vehicle12.jpeg"},
        {"image": "vehicle13.jpeg"},
        {"image": "vehicle14.jpeg"},
        {"image": "vehicle2.jpg"},
        {"image": "vehicle16.jpeg"},
        {"image": "vehicle17.jpeg"},
        {"image": "vehicle18.jpeg"},
        {"image": "vehicle19.jpeg"},
        {"image": "vehicle20.jpeg"},
        {"image": "vehicle21.jpeg"},
        {"image": "vehicle22.jpeg"},
        {"image": "vehicle23.jpeg"},
        {"image": "vehicle24.jpeg"},
        {"image": "vehicle25.jpeg"},
        {"image": "vehicle26.jpeg"},
        {"image": "vehicle27.jpeg"},
        {"image": "vehicle28.jpeg"},
        {"image": "vehicle29.jpeg"},
        {"image": "vehicle30.jpeg"},
        {"image": "vehicle31.jpeg"},
        {"image": "vehicle32.jpeg"},
        {"image": "vehicle33.jpeg"},
        {"image": "vehicle34.jpeg"},
        {"image": "vehicle35.jpeg"},
        {"image": "vehicle36.jpeg"},
        {"image": "vehicle37.jpeg"},
        {"image": "vehicle38.jpeg"},
        {"image": "vehicle39.jpeg"},
        {"image": "vehicle40.jpeg"},
        {"image": "vehicle41.jpeg"},
        {"image": "vehicle42.jpeg"},
        {"image": "vehicle43.jpeg"},
        {"image": "vehicle44.jpeg"},
        {"image": "vehicle45.jpeg"},
        {"image": "vehicle46.jpeg"},
        {"image": "vehicle47.jpeg"},
        {"image": "vehicle48.jpeg"},
        {"image": "vehicle3.jpg"},
        {"image": "vehicle50.jpeg"},
    ]
    return render(request, 'gallery.html', {'vehicles': vehicles})

# Listings page view (dynamic brand filtering)
def listings(request):
    brands = Listing.objects.values_list('brand', flat=True).distinct()
    return render(request, 'listings.html', {'brands': brands})

def listing(request, brand):
    vehicles = Listing.objects.filter(brand__iexact=brand)  # Case-insensitive
    return render(request, 'listing.html', {'vehicles': vehicles, 'brand': brand})

# Contact page view
def contact(request):
    return render(request, 'contact.html')

# About Us page view
def about(request):
    return render(request, 'about.html')
