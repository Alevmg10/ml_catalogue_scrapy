# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MlScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        precios = ['precio_usd', 'precio_bs']
        for precio in precios:
            valor = adapter.get(precio)
            adapter[precio] = float(valor)
        
        string_calidad = adapter.get('calidad')
        if '|' in string_calidad:
            string_calidad.split('|')


        return item
