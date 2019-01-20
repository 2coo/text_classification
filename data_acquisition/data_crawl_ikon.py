import scrapy
from readability import Readability

class IkonSpider(scrapy.Spider):
    name = 'ikon_spider'
    robotstxt_obey = True
    download_delay = 0.5
    user_agent = 'giva-crawler-for-nlp (giva9712@gmail.com)'
    autothrottle_enabled = True
    httpcache_enabled = True

    def start_requests(self):
        start_urls = [
            ('http://ikon.mn/l/1' , "politics"  ), # улс төр
            ('http://ikon.mn/l/2' , "economy"   ), # эдийн засаг
            ('http://ikon.mn/l/3' , "society"   ), # нийгэм
            ('http://ikon.mn/l/16', "health"    ), # эрүүл мэнд
            ('http://ikon.mn/l/4' , "world"     ), # дэлхийд
            ('http://ikon.mn/l/7' , "technology"), # технологи
        ]
        for index, url_tuple in enumerate(start_urls):
            url      = url_tuple[0]
            category = url_tuple[1]
            yield scrapy.Request(url, meta={'category': category})

    def parse(self, response):
        news =  Readability(str(response.body.decode('utf8'))).parse()
        if not news['title']:
            print("Could not find the title!", response.url)



            
