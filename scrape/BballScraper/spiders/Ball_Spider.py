import scrapy
from parseHelper import *
import time


# Run the python scrapes with the command : scrapy crawl players
class Ball_Spider(scrapy.Spider):

    name = 'players'
    secretCode = 'tDoYpc'
    handle_httpstatus_list = [404]   
    def start_requests(self):
        

        
        urls = readURLS()
        print(len(urls))
        input('')
        for index, url in enumerate(urls):
            if index == 0:
                yield scrapy.Request(url=url, callback=self.parse2, meta={'index':index})
            else:
                yield scrapy.Request(url=url, callback=self.parse, meta={'index':index})

    def parse(self, response):
        
        #filename = 'parse-%d.html' % response.meta['index'] 
        filename = 'parse-0.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        parseHTML()
    

        
    def parse2(self,response):
        with open('schoolList.html', 'wb') as f:
            f.write(response.body)
