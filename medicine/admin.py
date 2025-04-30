from django.contrib import admin
from medicine.models import Medicine, Category, Manufacturer

admin.site.register(Medicine)
admin.site.register(Category)
admin.site.register(Manufacturer)