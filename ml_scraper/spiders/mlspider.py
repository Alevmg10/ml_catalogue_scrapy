import scrapy
from ml_scraper.items import MlScraperItem

class MlspiderSpider(scrapy.Spider):
    name = "mlspider"
    allowed_domains = ["celulares.mercadolibre.com.ve"]
    start_urls = ["https://celulares.mercadolibre.com.ve/xiaomi/"]

    def parse(self, response):
        articulos = response.css('div.ui-search-result__wrapper')
        for articulo in articulos:
            articulos_url = articulo.css('a.ui-search-link').attrib['href']
            if articulos_url:
                yield scrapy.Request(url=articulos_url, callback=self.analizar_pagina_articulo, dont_filter=True)
        
        sig_pagina_url = response.css('li.andes-pagination__button--next a ::attr(href)').get()

        if sig_pagina_url is not None:
            yield response.follow(sig_pagina_url, callback=self.parse)

    def analizar_pagina_articulo(self, response):
        
        articulo_detalles = MlScraperItem()
        
        articulo_detalles['url'] = response.url
        articulo_detalles['titulo'] = response.css('h1.ui-pdp-title ::text').get()
        articulo_detalles['calidad'] = response.css('div.ui-pdp-header__subtitle span ::text').get()
        articulo_detalles['ciudad'] = response.css('div.ui-pdp-media__body .ui-pdp-media__text ::text').get()
        articulo_detalles['precio_usd'] = response.css('span.andes-money-amount meta ::attr(content)').get()
        articulo_detalles['precio_bs'] = response.css('div.ui-pdp-price__subtitles .andes-money-amount__fraction ::text').get()
        articulo_detalles['vendedor'] = response.css('div.ui-pdp-seller div.ui-pdp-seller__header__info-container a span ::text').get()
        articulo_detalles['vendedor_url'] = response.css('div.ui-box-component  a ::attr(href)').get()
        
        yield articulo_detalles