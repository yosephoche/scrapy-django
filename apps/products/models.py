from django.db import models

from apps.behaviors.models import Timestampable

class GroupProduct(Timestampable, models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name

class Product(Timestampable, models.Model):
    name = models.CharField(blank=True, max_length=500, help_text="product name")
    group = models.ForeignKey(GroupProduct, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(blank=True, max_length=500)
    subcategory = models.CharField(blank=True, max_length=500)
    description = models.TextField(blank=True)
    technical_data = models.TextField(blank=True)
    product_image_url = models.CharField(blank=True, max_length=500)
    brand_image_url = models.CharField(blank=True, max_length=500)
    url_source = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product"


class Variant(Timestampable, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    product_type = models.CharField(blank=True, null=True, max_length=100)
    model = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    technical_data = models.TextField(blank=True)


