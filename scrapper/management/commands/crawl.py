from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scrapper.scrapper import settings as my_settings

from scrapper.scrapper.spiders.product_spider import ProductSpider

class Command(BaseCommand):
    help = 'Simple Crawler'

    def handle(self, *args, **options):
        crawler_settings  = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(ProductSpider)
        process.start()