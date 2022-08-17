from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sreal.spiders.quotes_spider import srealSpider
process = CrawlerProcess(get_project_settings())
process.crawl(srealSpider)
process.start()

root = '/sreal/flaskServer.py'
exec(open(root).read())
