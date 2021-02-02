# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from apps.products.models import Product, GroupProduct
from .items import ProductItem

# class ScrapperPipeline:
#     def process_item(self, item, spider):
#         return item


class ProductPipeline():
    def process_item(self, item, spider):
        if isinstance(item, ProductItem):
            name = item["name"]
            group = item["group"]
            category = item["category"]
            subcategory = item["subcategory"]
            # description = item["description"]
            # technical_data = item["technical_data"]
            product_image_url = item["product_image_url"]
            brand_image_url = item["brand_image_url"]
            url_source = item["url_source"]

            try:
                group_instance = None
                if group is not None:
                    group_instance, created = GroupProduct.objects.get_or_create(name=group)

                create_product = Product.objects.get(name=name, group=group_instance)
            except BaseException:
                create_product = Product(
                    name=name,
                    group=group_instance,
                    category=category,
                    subcategory=subcategory,
                    product_image_url=product_image_url,
                    brand_image_url=brand_image_url,
                    url_source=url_source
                )

                create_product.save()

        return True