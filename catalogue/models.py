from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Size(models.Model):
    size = models.CharField()

    def __str__(self):
        return self.size
    
class ProductType(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    category = models.ManyToManyField(Category, blank=True, related_name='product')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.ManyToManyField(Size, blank=True, related_name='sizes')    
    # image = CloudinaryField('image', blank=True, null=True)
    image = models.ImageField(upload_to= 'product/',blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='type', null=True)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)

    def avail_units(self):
        try:
            return self.stock.qty # type: ignore
        except Stock.DoesNotExist:
            return 0

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='stock')
    qty = models.IntegerField()
    units_sold = models.IntegerField()

    def __str__(self):
        return f'{self.product.name}: {self.qty}' # type: ignore