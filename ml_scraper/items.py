# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MlScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    titulo = scrapy.Field()
    calidad = scrapy.Field()
    precio_usd = scrapy.Field()
    precio_bs = scrapy.Field()
    vendedor = scrapy.Field()
    vendedor_url = scrapy.Field()