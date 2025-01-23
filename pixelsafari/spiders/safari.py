import scrapy


class SafariSpider(scrapy.Spider):
    name = "safari"
    allowed_domains = ["pixelsafari.neocities.org"]
    start_urls = ["https://pixelsafari.neocities.org/stamps/"]



    def parse(self, response):
        imgs = response.xpath("/html/body/div/div[2]/main/center/img")
        for img in imgs:
            src = img.xpath("./@src").extract_first()
            yield {
                "src": src,
                "name":src.split("/")[-1].replace(".gif","")
            }


# //**[@class]
# /html/body/div/div[2]/main/center[2]/ul

# link =div.xpath(".//h3/a ")
# link.xpath("./text()").extract_first() <pega o texto do link
# link.xpath("./@href").extract_first() <pega o link
# img = div.xpath(".//img[contains(@class, "img-responsive")]@src").extract_first() <- pega a imagem que possui a classe image-reponsive
