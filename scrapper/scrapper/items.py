# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from apps.products.models import Product

# class ProductItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field()
#     price = scrapy.Field()
#     group = scrapy.Field()
#     category = scrapy.Field()
#     subcategory = scrapy.Field()
#     description = scrapy.Field()
#     technical_data = scrapy.Field()
#     product_image_url = scrapy.Field()
#     brand_image_url = scrapy.Field()
#     url_source = scrapy.Field()


class ProductItem(DjangoItem):
    django_model = Product