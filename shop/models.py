from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(unique=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    user_like = models.ManyToManyField(User)

    @property
    def discount_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        else:
            return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)


class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
    message = models.TextField()
    file = models.FileField(upload_to='images/')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class AttributeKey(models.Model):
    key_name = models.CharField(max_length=125, null=True)

    def str(self):
        return self.key_name


class AttiributeValue(models.Model):
    value_name = models.CharField(max_length=125, null=True)

    def str(self):
        return self.value_name


class ProductAttribute(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attiribute_key = models.ForeignKey('AttributeKey', on_delete=models.CASCADE)
    attiribute_value = models.ForeignKey('AttiributeValue', on_delete=models.CASCADE)
