from django.contrib import admin

from apps.products.models import Product, Variant

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "category", "subcategory", "product_image_url", "brand_image_url")
    list_filter = ("category", "group")
    search_fields = ("name", "description", )
    ordering = ("-id",)


admin.site.register(Product, ProductAdmin)
