#!/usr/bin/env python
#coding:utf-8
from django.contrib import admin
from app01 import  models
# Register your models here.

class BBS_admin(admin.ModelAdmin):
    list_display=('title','summary','author', 'signature','view_count','created_at')
    #需要元组
    list_filter=('created_at',)
    #通过引用外键
    search_fields=('title','author__user__username');

    def signature(self,obj):
        return obj.author.signature
    #修改signature 描述
    signature.short_description='hah'
admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)

