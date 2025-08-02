from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Address, TopMeasurement, BottomMeasurement
# Register your models here.

User = get_user_model()

# class CustomUserAdmin(UserAdmin):
#     model = User

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (None, {'fields': ('phone',)}),
#     )

#     add_fieldsets = (
#         *UserAdmin.add_fieldsets,
#         (None, {'fields': ('phone',)}),
#     )


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(TopMeasurement)
admin.site.register(BottomMeasurement)