from django.contrib import admin
from .models import Viloyat, Tuman, Stansiya, Osimlik, Hashorot, DataHashorot
# Register your models here.
models = [Viloyat, Tuman, Stansiya, Osimlik, Hashorot, DataHashorot]
for i in models:
    admin.site.register(i)
