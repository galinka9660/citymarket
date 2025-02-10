import scrapy
from my_scraper.app import add_product


class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["www.stephanis.com.cy"]
    start_urls = ["https://www.stephanis.com.cy/en/products/387164"]

    # imitates a browser because a website blocks a bot Scrapy (403 Error)
    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Getting a title and a price
        title = response.xpath("//title/text()").get()  
        price = response.css(".listing-details-heading.large-now-price.with-sale::text").get()
        
        # getting a description from a description table (labels and values)
        description = {}
        
        rows = response.css("table.product-details-specs-tbl tr")
        for row in rows:
            label = row.css("td.label::text").get()
            value = row.css("td.value::text").get()
            description[label.strip()] = value.strip()

        # checking availability, shows only the shops where item is available
        available_stores = []

        stores = response.css("li.tab-spec-list-item")
        for store in stores:
            location = store.css("div.stock-location-text::text").get()
            status_text = store.css("div.stockstatus div::text").get()

            if location and status_text and "out of stock" not in status_text.lower():
                available_stores.append({"location": location.strip(), "status": status_text.strip()})

        print(f"our title is: {title}")
        add_product(title)


        # what we write down in json file
        return {"title": title, "price": price, "description": description, "availability": available_stores}
        
        

