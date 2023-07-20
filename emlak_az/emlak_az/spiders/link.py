import scrapy


class LinkSpider(scrapy.Spider):
    name = "link"
    allowed_domains = ["emlak.az"]
    start_urls = ["https://emlak.az/elanlar/?ann_type=1&sort_type=0&page=595&page=1"]

    def parse(self, response):
        # hrefs = response.xpath('//div[@class="ticket clearfix pinned"]/div[@class="img"]/a/@href').getall()
        hrefs = response.xpath('//a[@class="m-trig" and @style="display:none;"]/@href').getall()

        for href in hrefs:
            yield {
                "href": href
            }
        # Extract the pagination link and follow it
        next_page_link = response.xpath('//a[contains(text(), "Növbəti")]/@href').get()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.parse)
