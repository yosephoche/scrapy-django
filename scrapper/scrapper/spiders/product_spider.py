import scrapy

from scrapper.scrapper.items import ProductItem
# from scrapper.items import ProductItem

# TODO :

class ProductSpider(scrapy.Spider):
    name = "product_scrapper"
    allowed_domains = ["weinmann-schanz.de"]
    schema = "https://www.weinmann-schanz.de"
    start_urls = ["https://www.weinmann-schanz.de/de/en/Home.html"]
    
    def parse(self, response):
        nav = response.css('div.HeaderElementMainNavWidth > div#mainnavi2')

        for category in nav.css('ul > li'):
            link = category.css('div.level1 a::attr(href)').get()
            group = category.css('div.level1 a::text').extract_first()
            
            if group is not None and group != 'Promotions':
                if link is not None:
                    link = response.urljoin(link)
                    request = scrapy.Request(url=link, callback=self.parse_group_item)
                    request.meta['group'] = group
                    yield request

    def parse_group_item(self, response):
        sub_nav = response.css('.SubNaviStdBox')
        group = response.meta.get('group')
        for sub in sub_nav.css('ul.navLevel1 > li'):
            link = sub.css('a::attr(href)').get()
            name = sub.css('a::text').extract_first()
            
            if link is not None:
                link = response.urljoin(link)
                # this wil go to scrape this url
                # /de/en/Electro/New-in-Range-sid185574.html
                request = scrapy.Request(url=link, callback=self.parse_category)
                request.meta['category'] = name
                request.meta['group'] = group
                yield request

    def parse_category(self, response):
        element = response.css('.SubNaviStdBox')
        category = response.meta.get('category')
        group = response.meta.get('group')
        for el in element.css('ul.navLevel2 > li'):
            link = el.css('a::attr(href)').get()
            subcategory = el.css('a::text').extract_first()
            if link is not None:
                link = response.urljoin(link)
                # this will scrape this url 
                # /de/en/Installation/New-in-Range/Pipe-systems.html
                request = scrapy.Request(url=link, callback=self.parse_subcategory)
                request.meta['category'] = category
                request.meta['subcategory'] = subcategory
                request.meta['group'] = group
                yield request

    def parse_subcategory(self, response):
        element = response.css('.SubNaviStdBox')
        category = response.meta.get('category')
        subcategory = response.meta.get('subcategory')
        group = response.meta.get('group')
        
        for product in element.css('ul.navLevel3 > li'):
            link = product.css('a::attr(href)').get()
            if link is not None:
                link = response.urljoin(link)
                request = scrapy.Request(url=link, callback=self.parse_product)
                request.meta['category'] = category
                request.meta['subcategory'] = subcategory
                request.meta['group'] = group
                yield request
    
    def parse_product(self, response):
        # .ArtGrpDetailHeadArtGrpNameBox > h1:nth-child(1)
        category = response.meta.get('category')
        subcategory = response.meta.get('subcategory')
        group = response.meta.get('group')

        url = response.url
        item = ProductItem()
        
        name = response.css('.ArtGrpDetailHeadArtGrpNameBox > h1:nth-child(1)::text').extract_first()
        price = response.css('.sp > span:nth-child(1)::text').extract_first()
        brand_image_url = response.css('.ArtGrpDetailHeadArtGrpPicBox > img:nth-child(1)::attr(src)').get()
        product_image_url = response.css('.Zoom > img:nth-child(1)::attr(src)').get()
        
        item["name"] = name
        # item["price"] = price
        item["category"] = category
        item["subcategory"] = subcategory
        item["group"] = group
        item["brand_image_url"] = response.urljoin(brand_image_url)
        item["product_image_url"] = response.urljoin(product_image_url)
        item["url_source"] = response.url
        
        yield item