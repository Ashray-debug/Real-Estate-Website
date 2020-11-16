from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('contacts/', include('contacts.urls')),
    path('seller/', include('seller.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)