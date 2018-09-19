# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from mycms.models import Articles, ScrapyLogs, Baikes, Zhidaos, Images, Youkus, Wordroots



class WordrootsItem(DjangoItem):
    django_model = Wordroots

class ArticlesItem(DjangoItem):
    django_model = Articles

class ScrapyLogsItem(DjangoItem):
    django_model = ScrapyLogs


class BaikesItem(DjangoItem):
    django_model = Baikes


class ZhidaosItem(DjangoItem):
    django_model = Zhidaos


class ImagesItem(DjangoItem):
    django_model = Images


class YoukusItem(DjangoItem):
    django_model = Youkus