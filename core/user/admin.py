from django.contrib import admin
from .models import CustomUser, UserProfile, Address, TopMeasurement, BottomMeasurement
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(TopMeasurement)
admin.site.register(BottomMeasurement)