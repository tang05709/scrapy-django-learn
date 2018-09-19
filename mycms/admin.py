from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponseRedirect

# Register your models here.
from .models import Wordroots, Categories, Articles, Baikes, Zhidaos, Images, Youkus, Tags, ScrapyRules, ScrapyLogs, ScrapyTasks


class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')

  # actions = ['get_all', ]




class WordrootAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_done', 'created_at', 'catch_page')

  def catch_page(self, obj):
    return format_html('<a href="">ddd</a>')



class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'click_count', 'order', 'created_at')

class BaikeAdmin(admin.ModelAdmin):
  list_display = ('title', 'url', 'created_at')


class ZhidaoAdmin(admin.ModelAdmin):
  list_display = ('title', 'url', 'created_at')


class ImageAdmin(admin.ModelAdmin):
  list_display = ('image', 'url', 'created_at')


class YoukuAdmin(admin.ModelAdmin):
  list_display = ('video', 'url', 'created_at')



class TagAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')



class ScrapyRuleAdmin(admin.ModelAdmin):
  list_display = ('name', 'url', 'created_at')



class ScrapyTaskAdmin(admin.ModelAdmin):
  list_display = ('start_date_at', 'start_time_at', 'task_cycle',  'is_done', 'created_at')

  actions = ['make_scrapy']

  def make_scrapy(self, request, queryset):
    return HttpResponseRedirect('/admin/')

  make_scrapy.short_description = 'make scrapy'


class ScrapyLogAdmin(admin.ModelAdmin):
  list_display = ('url', 'created_at')

  actions = ['make_scrapy']

  def make_scrapy(self):
    pass

  make_scrapy.short_description = 'make scrapy'


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Wordroots, WordrootAdmin)
admin.site.register(Articles, ArticleAdmin)
admin.site.register(Baikes, BaikeAdmin)
admin.site.register(Zhidaos, ZhidaoAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Youkus, YoukuAdmin)
admin.site.register(Tags, TagAdmin)
admin.site.register(ScrapyRules, ScrapyRuleAdmin)
admin.site.register(ScrapyTasks, ScrapyTaskAdmin)
admin.site.register(ScrapyLogs, ScrapyLogAdmin)


