from django.contrib import admin

from . models import Category,Product,ProductImage,Review,Wishlist
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug":('name', )}

admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Wishlist)
