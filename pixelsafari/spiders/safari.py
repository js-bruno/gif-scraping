import scrapy


class SafariSpider(scrapy.Spider):
    name = "safari"
    allowed_domains = ["pixelsafari.neocities.org"]
    start_urls = ["https://pixelsafari.neocities.org"]


    def parse(self, response):
        site_title = response.xpath(".//title/text()").extract_first()

        navbar = response.xpath(".//nav[contains(@id, 'navbar')]")
        navbar_links = navbar.xpath(".//li/a/@href").extract()

        for link in navbar_links:
            yield scrapy.Request(url=link, callback=self.parse_and_get_gifs)
            # yield {gifs: all_gifs,  "next_page": scrapy.Request(url=link, callback=self.parse)} 

    def parse_and_get_gifs(self, response):
        domain_url =  response.url.rsplit("/", 2)[0]

        imgs = response.xpath(".//main/center/img")
        sources = []
        for img in imgs:
            src = img.xpath("./@src").extract_first()
            image_source = domain_url + src
            self.log(f"{image_source}")
            sources.append(image_source)

        yield {"sources": sources, "folder": src.split("/")[1]}

    def extract_font_name(response):
        welcome_tag = response.xpath(".//span[contains(text(), 'Welcome')]")


# //**[@class]
# /html/body/div/div[2]/main/center[2]/ul

# link =div.xpath(".//h3/a ")
# link.xpath("./text()").extract_first() <pega o texto do link
# link.xpath("./@href").extract_first() <pega o link
# img = div.xpath(".//img[contains(@class, "img-responsive")]@src").extract_first() <- pega a imagem que possui a classe image-reponsive
# response.xpath(".//span[contains(text(), 'Welcome')]/following-sibling::strong/a/@title") <- Pega a tag que esta dentro da selecionada
# response.xpath(".//span[contains(text(), 'Welcome')]/following-sibling::strong/a/@title") <- Pega a tag que esta dentro da selecionada
