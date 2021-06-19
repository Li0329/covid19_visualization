from django.db import models

# Create your models here.

"""
    疫情信息表主要包括世界信息和国内信息两部分
    主要包括的字段有
    - 地区/国家id
    - 地区/国家名字
    - 确诊人数
    - 现行确诊人数
    - 死亡人数
    - 治愈人数
    - 近期确诊人数
"""


class World(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=250)
    confirmed = models.IntegerField()
    curConfirmed = models.IntegerField()
    died = models.IntegerField()
    cured = models.IntegerField()
    confirmedRelative = models.IntegerField()


class China(models.Model):
    id = models.IntegerField(primary_key=True)
    area = models.CharField(max_length=250)
    confirmed = models.IntegerField()
    curConfirmed = models.IntegerField()
    died = models.IntegerField()
    cured = models.IntegerField()
    confirmedRelative = models.IntegerField()


class Heatmap(models.Model):
    data = models.JSONField()