from django.urls import path
from . import views

urlpatterns = [
    # Home and static pages
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # Listings routes
    path('listings/', views.listings, name='listings'),  # Shows all vehicle brands
    path('listings/<str:brand>/', views.listing, name='listing'),  # Shows listings for a specific brand
]
