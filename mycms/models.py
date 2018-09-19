from django.db import models
import django.utils.timezone as timezone

# Create your models here.

# Create your models here.
class Categories(models.Model):
  # 文章分类
  name = models.CharField(max_length=200, verbose_name = "分类名称")
  parent = models.ForeignKey('self', default=0, on_delete=models.DO_NOTHING, null = True, blank = True, verbose_name = "上级分类")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = '分类管理'


class Wordroots(models.Model):
  # 爬取的词
  SHIRT_SIZES = (
    (0, '否'),
    (1, '是'),
  )
  name = models.CharField(max_length=255, verbose_name = "词语")
  is_done = models.IntegerField(default=0,  choices=SHIRT_SIZES, verbose_name = "是否采集")
  category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, verbose_name = "分类名称")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")


  class Meta:
    verbose_name_plural = '词库管理'


class Articles(models.Model):
  # 抓取的数据组合的文章
  wordroot = models.CharField(max_length=255, verbose_name = "词根")
  title = models.CharField(max_length=255, verbose_name = "标题")
  content = models.TextField(null = True, blank = True, verbose_name = "内容组合")
  category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, verbose_name = "分类名称")
  image = models.ImageField(max_length=255, null = True, blank = True, verbose_name = "图片")
  video = models.FileField(max_length=255, null = True, blank = True, verbose_name = "视频")
  question = models.CharField(max_length=255, null = True, blank = True,  verbose_name = "问答问题")
  answer = models.TextField(null = True, blank = True, verbose_name = "问答回答")
  baike_title = models.CharField(max_length=255, null = True, blank = True, verbose_name = "百科标题")
  baike_content = models.TextField(null = True, blank = True, verbose_name = "百科内容")
  seo_keywords = models.CharField(max_length=255, null = True, blank = True, verbose_name = "关键词")
  seo_description = models.CharField(max_length=255, null = True, blank = True, verbose_name = "描述")
  click_count = models.IntegerField(default=0, verbose_name = "点击")
  order = models.IntegerField(default=0, verbose_name = "排序")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
     verbose_name_plural = '文章管理'

    
class Baikes(models.Model):
  # 百科
  wordroot_text = models.CharField(max_length=255, verbose_name = "词根")
  wordroot_id = models.IntegerField(default=0, null = True, blank = True, verbose_name = "词根id, 可空")
  url = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "爬取链接")
  title = models.CharField(max_length=255, null = True, blank = True, verbose_name = "标题")
  content = models.TextField(null = True, blank = True, verbose_name = "内容")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = '百度百科'


class Zhidaos(models.Model):
  # 知道
  wordroot_text = models.CharField(max_length=255, verbose_name = "词根")
  wordroot_id = models.IntegerField(default=0, null = True, blank = True, verbose_name = "词根id, 可空")
  url = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "爬取链接")
  title = models.CharField(max_length=255, null = True, blank = True, verbose_name = "标题")
  content = models.TextField(null = True, blank = True, verbose_name = "内容")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = '百度知道'


class Images(models.Model):
  # 图片
  wordroot_text = models.CharField(max_length=255, verbose_name = "词根")
  wordroot_id = models.IntegerField(default=0, null = True, blank = True, verbose_name = "词根id, 可空")
  url = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "爬取链接")
  image = models.CharField(max_length=255, null = True, blank = True, verbose_name = "图片链接")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = '百度图片'


class Youkus(models.Model):
  # 优酷
  wordroot_text = models.CharField(max_length=255, verbose_name = "词根")
  wordroot_id = models.IntegerField(default=0, null = True, blank = True, verbose_name = "词根id, 可空")
  url = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "爬取链接")
  video = models.CharField(max_length=255, null = True, blank = True, verbose_name = "视频分享地址")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = '优酷视频'

class Tags(models.Model):
  #标签
  name = models.CharField(max_length=255, verbose_name = "标签名称")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = '标签管理'

class TagMaps(models.Model):
  article = models.ForeignKey(Articles, on_delete=models.DO_NOTHING)
  tag = models.ForeignKey(Tags, on_delete=models.DO_NOTHING)


class ScrapyRules(models.Model):
  # 爬虫链接及规则
  name = models.CharField(max_length = 255, verbose_name = "爬取网站")
  url = models.CharField(max_length = 255, verbose_name = "爬取链接")
  search_rules = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "搜索爬取规则")
  title_rules = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "标题爬取规则")
  content_rules = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "内容爬取规则")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = "链接管理"


class ScrapyLogs(models.Model):
  # 爬虫日志
  url = models.CharField(max_length = 255, verbose_name = "爬取链接")
  title = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "页面标题")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = "爬虫日志"


class ScrapyTasks(models.Model):
  # 定时任务
  # 爬取的词
  SHIRT_SIZES = (
    ('0', '否'),
    ('1', '是'),
  )
  CYCLE_TYPE = (
    ('0', '按指定日期时间执行'),
    ('1', '按指定时间每天执行'),
    ('2', '按指定时间每周执行'),
    ('3', '按指定时间每月执行'),
  )
  start_date_at = models.DateField(default = timezone.now, verbose_name = "开始时间")
  start_time_at = models.TimeField(default = timezone.now, verbose_name = "开始时间")
  task_cycle = models.IntegerField(default=0,  choices=CYCLE_TYPE, verbose_name = "定时方式")
  is_done =  models.IntegerField(default=0,  choices=SHIRT_SIZES, verbose_name = "是否包含已采集")
  created_at = models.DateTimeField(default = timezone.now, verbose_name = "添加日期")
  updated_at = models.DateTimeField(default = timezone.now, verbose_name = "修改日期")

  class Meta:
    verbose_name_plural = "爬虫任务"

