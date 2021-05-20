import scrapy
from scrapy.selector import Selector
from mybot.items import ArticleItem

class MySpider(scrapy.Spider):
	name="test"
	start_urls = ['http://www.bbc.com/news/world-asia-china-40603059', ]

	def parse(self, response):
		
		
		item = ArticleItem()
		parsed_items = []
		item['title'] = response.xpath('.//div[@class="story-body"]/h1/text()').extract_first()
		item['article'] = response.xpath('.//div[@class="story-body__inner"]/p/text()').extract()
		
		
		parsed_items.append(item)
		return parsed_items



# 		