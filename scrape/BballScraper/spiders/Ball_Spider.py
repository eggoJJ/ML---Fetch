import scrapy
from parseHelper import *
import time


# Run the python scrapes with the command : scrapy crawl players
class Ball_Spider(scrapy.Spider):

    name = 'players'
    secretCode = 'tDoYpc'
    handle_httpstatus_list = [404]   
    def start_requests(self):
        urls = [ 'https://www.sports-reference.com/cbb/schools/duke/2017.html',
                 'https://www.sports-reference.com/cbb/schools/duke/2016.html',
                 'https://www.sports-reference.com/cbb/schools/duke/2015.html',
                 'https://www.sports-reference.com/cbb/schools/duke/2014.html',
                 'https://www.sports-reference.com/cbb/schools/duke/2013.html'
                 
        ]
        for index, url in enumerate(urls):
            yield scrapy.Request(url=url, callback=self.parse, meta={'index':index})

    def parse(self, response):
        
        #filename = 'parse-%d.html' % response.meta['index'] 
        filename = 'parse-0.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        parseHTML()
    

        
