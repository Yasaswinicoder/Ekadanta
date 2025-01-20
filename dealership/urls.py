from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('', views.home, name='home'),  # Root URL points to home
    path('listings/', include('listings.urls')),  # Include app-specific routes for listings
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
