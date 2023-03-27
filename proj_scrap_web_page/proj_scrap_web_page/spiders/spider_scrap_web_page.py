import scrapy

class MySpider(scrapy.Spider):
    name = "spider_scrap_web_page"

    def __init__(self, url=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

    def parse(self, response):
        # Define your parsing logic here
        pass
