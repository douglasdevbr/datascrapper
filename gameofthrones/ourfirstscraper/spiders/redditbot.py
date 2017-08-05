import scrapy
from scrapy.http import Request


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    ''' allowed_domains = ['http://www.stone.superged.com.br']'''
    start_urls = ['http://200.221.196.98:8086/stone/j_spring_security_check']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'j_username': '273.601.108-23', 'j_password': 'magda141'},
            callback=self.after_login)
        
        

    def after_login(self, response):
        if "senha incorreto(s)" in response.body:
             self.logger.error("Login failed!")
        else:
            self.logger.error("Login succeeded!")
            self.log("respostaaa")
            item = {
                'dados' : response.body
             }

             
            return scrapy.Request(url="http://200.221.196.98:8086/stone/pages/cliente/finalizado.jsf", callback=self.parse_tastypage)
            
           
       #Extracting the content using css selectors
        '''
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()
        '''
        #Give the extracted content row wise
        '''
        scraped_info = {
                'dados' : raw
                
            }
        
        for item in zip(titles,votes,times,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'comments' : item[3],
            }
        '''
            #yield or give the scraped info to scrapy
        ''' yield scraped_info'''

    def  parse_tastypage(self, response):

        raw = response.body
        scraped_info = {
                'dados' : raw
                
            }
        self.log("respostaaa2222222")
        self.log(response.body)
        yield scraped_info

