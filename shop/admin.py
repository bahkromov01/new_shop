
from django.contrib import admin

from shop.models import Category, Product, Group, Comment, Image, ProductAttribute


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'image']
    list_display = ['title', 'image', 'slug']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'image',]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = []

    def save_model(self, request, obj, form, change):
        if not change:  # Only set user on creation, not on updates
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(ProductAttribute)