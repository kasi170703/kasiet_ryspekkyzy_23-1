from django.db import models


# Create your models here.


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Category(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    rate = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,related_name='products')

    def __str__(self):
        return self.name
