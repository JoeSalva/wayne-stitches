from django.contrib import admin
from .models import Product, Category, Stock, Size

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Size)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ("name",),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ("name",),
    }