from .models import Baikes, Zhidaos, Images, Youkus, Wordroots
from scrapy import cmdline
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def report(request):
  woodroot = Wordroots.objects.get(pk = 1)
  process = CrawlerProcess(get_project_settings())
  process.crawl('mycms', domain='http://localhost:6800/')
  process.start()
  #cmdline.execute(['scrapy', 'crawl', 'mycms'])
  #cmdline.execute([
  #  'scrapy', 'crawl', 'mycms',
  #  '-a', 'woodroot_text=' + woodroot.name, '-a', 'woodroot_id=' + 1])




  
