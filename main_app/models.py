from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    image = models.ImageField(upload_to="")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=300)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="")
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="products")
    price = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name


