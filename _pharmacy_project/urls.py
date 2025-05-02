from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # first party urls
    path('', home, name='home'),
    path('user/', include('users.urls')),
    path('medicine/', include('medicine.urls')),
]
