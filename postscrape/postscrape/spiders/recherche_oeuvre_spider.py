import scrapy
from utils.url_funcs import get_recherche_oeuvre_url
from ..items import ROItem

class ROSpider(scrapy.Spider):
    name = "ro"
    start_urls = get_recherche_oeuvre_url()

    def parse(self, response):
        ro_items = ROItem()

        for each_painting in response.css('div.oeuvre_container'): 
            title = each_painting.css('div.oeuvre_infos h3 a::text').get()
            prix = each_painting.css('div.oeuvre_price_container div div::text').get()
            img_url = each_painting.css('div.meilleur-vente img::attr(data-src)').get()
            
            ro_items['title'] = title
            ro_items['prix'] = prix
            ro_items['img_url'] = img_url
        
            yield ro_items