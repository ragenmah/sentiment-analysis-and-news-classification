import scrapy
from scrapy.selector import Selector, HtmlXPathSelector, XmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from mybot.items import ArticleItem

class MySpider(scrapy.Spider):
	name = "article"
	start_urls = ['http://feeds.bbci.co.uk/news/rss.xml?edition=uk',
			]

	

	def parse(self, response):
	    xxs=XmlXPathSelector(response)
	    links = xxs.select("//item/link/text()").extract()
	    return [Request(x, callback=self.parse_link) for x in links]
	
	
	
	def parse_link(self, response):
		hxs = HtmlXPathSelector(response)
		# yield{
		# 	'article':hxs.xpath('//div[@class="story-body__inner"]/p/text()').extract(),
		# 	'title':hxs.xpath('//div[@class="story-body"]/h1/text()').extract(),
		# 	'description':hxs.xpath('//div[@class="story-body__inner"]/p/text()').extract_first(),
		# }

		item = ArticleItem()
		parsed_items = []
		item['pubDate'] = hxs.xpath('.//div[@class="date date--v2"]/text()').extract_first()
		item['title'] = hxs.xpath('.//div[@class="story-body"]/h1/text()').extract_first()

		# item['article'] = hxs.xpath('.//div[@class="story-body__inner"]/p/text()').extract()
		article_list = hxs.xpath('.//div[@class="story-body__inner"]/p/text()').extract()
		article = ' '.join(article_list).strip(' \n')
		item['article'] = article
		 # body_list = response.xpath("//" + XpathUtil.xpath_for_class("story-body__inner") + "//p/text()").extract()
   #      body = ' '.join(body_list).strip(' \n')
		item['description'] = hxs.xpath('.//div[@class="story-body__inner"]/p/text()').extract_first()
		item['url'] = response.url	
		item['image_url'] = hxs.xpath('//span[@class="image-and-copyright-container"]/img/@src').extract_first()
		
		parsed_items.append(item)
		return parsed_items

