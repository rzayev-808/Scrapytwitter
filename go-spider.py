from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from tutorial.spiders.quotes_spider import TweetScraper
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(TweetScraper)
process.start()