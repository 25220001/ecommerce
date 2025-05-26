from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,db_index=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        verbose_name_plural="categories"


    def __str__(self):

        return self.name
    
    def get_absolute_url(self):
    
        return reverse('list-category',args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # rating = models.FloatField(default=0.0)
    size=models
    # @property
    # def review_count(self):
    #     return self.reviews.count()
    
    main_image = models.ImageField(upload_to='images/')
    
    # is_best_seller = models.BooleanField(default=False)
    # is_top_rated = models.BooleanField(default=False)

    detailed_description = models.TextField(default=None,blank=True)
    specifications = models.TextField(default=None,blank=True)

    # color_options = models.JSONField(default=list)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product',null=True)  # ✅ Fixed

    related_products = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return reverse('product-info',args=[self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='images/')
    color=models.TextField(default=None)
    def __str__(self):
        return self.product.name
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
