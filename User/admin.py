from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = '疫情可视化系统后台'
admin.site.site_title = '疫情可视化系统后台'
admin.site.index_title = '疫情可视化系统后台'
admin.site.register(models.UserInfo)