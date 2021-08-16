import scrapy

class Ku137Spider(scrapy.Spider):
    name = 'ku137'
    allowed_domains = ['ku137.net']
    start_urls = ['https://www.ku137.net/b/1/']
    head='https://www.ku137.net/b/1/'
    limit=5
    num=0

    def parse(self, response):
        hrefs=response.xpath('//div[@class="m-list ml1"]//li/a/@href').getall()
        for href in hrefs:
            yield scrapy.Request(href, callback=self.parse_d)
        self.num+=1
        if self.num==self.limit:
            return
        nextPage=response.xpath('//div[@class="page"]/a[last()-1]/@href')
        if  len(nextPage)>0:
            nextPage=nextPage.get()
            nextPage=self.head+nextPage
            yield scrapy.Request(nextPage, callback=self.parse)

    def parse_d(self,response):
        srcs=response.xpath('//div[@class="content"]/img/@src').getall()
        urlhead=response.xpath('//div[@class="w1200"]/a[last()]/@href').get()
        yield {'image_urls':srcs}
        nextPage=response.xpath('//div[@class="page"]/a[last()]/@href')
        if len(nextPage)>0:
            nextPage=nextPage.get()
            url=urlhead+nextPage
            yield scrapy.Request(url, callback=self.parse_d)