
import scrapy
from scrapy_splash import SplashRequest
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware
from scrapycms.items import WordrootsItem, ScrapyLogsItem, ArticlesItem, BaikesItem, ZhidaosItem, ImagesItem, YoukusItem
import json
import requests
from mycms.models import ScrapyRules

class TupianSpider(scrapy.Spider):
  name = "mycms"
  keywords = '水星'

  """wordroot_text = ''
  wordroot_id = 0
  keywords = ''
  def __init__(self, wordroot_text, wordroot_id):
    self.wordroot_text = wordroot_text
    self.wordroot_id = wordroot_id
    self.keywords = wordroot_text
    super(TupianSpider, self).__init__(*args, **kwargs)"""

  rules = ScrapyRules.objects.all()
  # start_urls 要爬取的url
  start_urls = []
  # 需要爬取搜索页的链接, 内容页的标题和内容,
  # 百度知道爬取问题和最佳答案
  # 百度图片爬取除去广告图片之外的第一张图片
  # 优酷视频爬取分享链接的第一个emue链接
  # 百度百科
  baike_search_rule = ''
  baike_title_rule = ''
  baike_content_rule = ''
  # 百度知道
  zhidao_search_rule = ''
  zhidao_title_rule = ''
  zhidao_content_rule = ''
  # 百度图片
  image_search_rule = ''
  # 优酷视频
  youku_search_rule = ''
  youku_title_rule = ''
  youku_video_rule = ''

  for rule in rules:
    new_url = rule.url % keywords
    start_urls.append(new_url)
    if 'baike.baidu' in new_url:
      baike_search_rule = rule.search_rules
      baike_title_rule = rule.title_rules
      baike_content_rule = rule.content_rules

    if 'zhidao.baidu' in new_url:
      zhidao_search_rule = rule.search_rules
      zhidao_title_rule = rule.title_rules
      zhidao_content_rule = rule.content_rules

    if 'image.baidu' in new_url:
      image_search_rule = rule.search_rules

    if 'so.youku' in new_url:
      youku_search_rule = rule.search_rules
      youku_title_rule = rule.title_rules
      youku_video_rule = rule.content_rules

  #start_urls = [
  #  "https://baike.baidu.com/search?word=%s&pn=0&rn=0&enc=utf8" % keywords,
  #  "https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%s" % keywords,
  #  "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%s" % keywords,
  #  "https://so.youku.com/search_video/q_%s" % keywords,
  #]

  
  def start_requests(self):
    for url in self.start_urls:
      yield SplashRequest(url, self.parse, args={'wait': '0.5'})
            
  def parse(self, response):
    current_url = response.url
    # 百度百科
    if 'baike.baidu' in current_url:
      link = response.xpath(self.baike_search_rule)
      href = link.xpath('@href').extract_first()
      text = link.xpath('text()').extract_first()

      logs_item = ScrapyLogsItem()
      logs_item['url'] = current_url
      logs_item['title'] = 'search:' + text
      logs_item.save()
      
      yield scrapy.Request(href, self.content_parse)


    #百度知道
    if 'zhidao.baidu' in current_url:
      link = response.xpath(self.zhidao_search_rule)
      href = link.xpath('@href').extract_first().strip()
      text = link.xpath('string(.)').extract_first()
      logs_item = ScrapyLogsItem()
      logs_item['url'] = current_url
      logs_item['title'] = 'search:' + text
      logs_item.save()

      yield scrapy.Request(href, self.content_parse)

    #百度图片
    if 'image.baidu' in current_url:
      logs_item = ScrapyLogsItem()
      logs_item['url'] = current_url
      logs_item['title'] = 'search: ' + self.keywords
      logs_item.save()

      img = response.xpath(self.image_search_rule).extract_first()

      # 获取图片后缀
      
      # 下载图片
      r = requests.get(img)
      with open('./img/image3.png', 'wb') as f:
        f.write(r.content)

      
      img_item = ImagesItem()
      img_item['wordroot_text'] = self.keywords
      img_item['wordroot_id'] = 1
      img_item['url'] = current_url
      img_item['image'] = img
      yield img_item

    #优酷视频
    if 'so.youku' in current_url:
      link = response.xpath(self.youku_search_rule)
      href = link.xpath('@href').extract_first()
      href = 'https://' + href
      text = link.xpath('text()').extract_first()

      logs_item = ScrapyLogsItem()
      logs_item['url'] = current_url
      logs_item['title'] = 'search: ' + text
      logs_item.save()

      yield scrapy.Request(href, self.content_parse)


  def content_parse(self, response):
    content_url = response.url

    # 要保存的数据
    #article = ArticlesItem()
    #article['workroot'] = self.keywords
    #article['category_id'] = 1
    #article['seo_keywords'] = self.keywords
    #article['seo_description'] = self.keywords
    #article['click_count'] = 1
    #article['order'] = 100


    # 百度百科
    if 'baike.baidu' in content_url:
      title = response.xpath(self.baike_title_rule).extract_first()
      content_list = response.xpath(self.baike_content_rule).xpath("string(.)").extract()
      content_res = " ".join(content_list)

      logs_item = ScrapyLogsItem()
      logs_item['url'] = content_url
      logs_item['title'] = 'content: ' + title
      logs_item.save()

      baike_item = BaikesItem()
      baike_item['wordroot_text'] = self.keywords
      baike_item['wordroot_id'] = 1
      baike_item['url'] = content_url
      baike_item['title'] = title
      baike_item['content'] = content_res
      yield baike_item

    #百度知道
    if 'zhidao.baidu' in content_url:
      title = response.xpath(self.zhidao_title_rule).extract_first()
      content_list = response.xpath(self.zhidao_content_rule).xpath("string(.)").extract()
      #content_res = " ".join(content_list)

      logs_item = ScrapyLogsItem()
      logs_item['url'] = content_url
      logs_item['title'] = 'content: ' + title
      logs_item.save()

      zhidao_item = ZhidaosItem()
      zhidao_item['wordroot_text'] = self.keywords
      zhidao_item['wordroot_id'] = 1
      zhidao_item['url'] = content_url
      zhidao_item['title'] = title
      zhidao_item['content'] = content_list
      yield zhidao_item

    #优酷视频
    if 'v.youku' in content_url:
      title = response.xpath(self.youku_title_rule).extract_first()
      video_url = response.xpath(self.youku_video_rule).extract_first()

      logs_item = ScrapyLogsItem()
      logs_item['url'] = content_url
      logs_item['title'] = 'content: ' + title
      logs_item.save()

      youku_item = YoukusItem()
      youku_item['wordroot_text'] = self.keywords
      youku_item['wordroot_id'] = 1
      youku_item['url'] = content_url
      youku_item['video'] = video_url
      yield youku_item





        