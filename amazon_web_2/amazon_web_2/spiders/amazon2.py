import scrapy
from ..items import AmazonWeb2Item

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        "https://www.amazon.in/s?k=bikes&crid=80UOMNI20AK0&sprefix=bikes%2Caps%2C351&ref=nb_sb_noss_2"
    ]

    def parse(self, response):
        items = AmazonWeb2Item()

        product_name = response.css(".a-color-base.a-text-normal::text").extract()
        product_age_use = response.css(".a-spacing-top-mini span::text").extract()
        product_price = response.css(".a-price-whole::text").extract()
        product_link = response.css(".s-image::attr(src)").extract()

        items['product_name'] = product_name
        items['product_age_use'] = product_age_use
        items['product_price'] = product_price
        items['product_link'] = product_link

        yield items

        next_page = 'https://www.amazon.in/s?k=bikes&page=' + str(AmazonSpider.page_number) + '&crid=80UOMNI20AK0&qid=1694578577&sprefix=bikes%2Caps%2C351&ref=sr_pg_2'
        if AmazonSpider.page_number <= 7:  # Change this condition if needed
            AmazonSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
