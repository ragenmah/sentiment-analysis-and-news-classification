from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from mybot.items import FeedItem

class NewsSpider(BaseSpider):
	name = "bbc"
	allowed_domains = ["example.com"]
	start_urls = ['http://feeds.bbci.co.uk/news/rss.xml', ]

	def parse(self, response):
		sel = Selector(response)
		items = sel.xpath('//item')
		parsed_items = []
		for elements in items:
			item = FeedItem()
			item['site'] = 'BBC-News'
			item['title'] = elements.xpath('./title/text()').extract_first()
			item['description'] = elements.xpath('./description/text()').extract_first()
			item['url'] = elements.xpath('./link/text()').extract_first()
			item['pubDate'] = elements.xpath('./pubDate/text()').extract_first()
			parsed_items.append(item)
		return parsed_items