# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import teamnoticeViews

urlpatterns = [

    #  定义添加团队公告的url地址响应方法，跳转到 teamnoticeView的tianjiateamnotice方法
    url(r'^tianjiateamnotice/$', teamnoticeViews.tianjiateamnotice, name='tianjiateamnotice'),

    #  定义处理添加团队公告的url地址响应方法，跳转到 teamnoticeView的tianjiateamnoticeact方法
    url(r'^tianjiateamnoticeact/$', teamnoticeViews.tianjiateamnoticeact, name='tianjiateamnoticeact'),

    #  定义跳转修改团队公告的url地址响应方法，跳转到 teamnoticeView的xiugaiteamnotice方法
    url(r'^xiugaiteamnotice/(?P<id>[0-9]+)$', teamnoticeViews.xiugaiteamnotice, name='xiugaiteamnotice'),

    #  定义处理修改团队公告的url地址响应方法，跳转到 teamnoticeView的xiugaiteamnoticeat方法
    url(r'^xiugaiteamnoticeact/$', teamnoticeViews.xiugaiteamnoticeact, name='xiugaiteamnoticeact'),

    #  定义跳转管理团队公告的url地址响应方法，跳转到 teamnoticeView的teamnoticeguanli方法
    url(r'^teamnoticeguanli/$', teamnoticeViews.teamnoticeguanli, name='teamnoticeguanli'),

    #  定义跳转查看团队公告的url地址响应方法，跳转到 teamnoticeView的teamnoticechakan方法
    url(r'^teamnoticechakan/$', teamnoticeViews.teamnoticechakan, name='teamnoticechakan'),

    #  定义处理删除团队公告的url地址响应方法，跳转到 teamnoticeView的shanchuteamnotice方法
    url(r'^shanchuteamnoticeact/(?P<id>[0-9]+)$', teamnoticeViews.shanchuteamnoticeact, name='shanchuteamnoticeact'),

    #  定义跳转搜索团队公告的url地址响应方法，跳转到 teamnoticeView的sousuoteamnotice方法
    url(r'^sousuoteamnotice/$', teamnoticeViews.sousuoteamnotice, name='sousuoteamnotice'),

    #  定义团队公告详情的url地址响应方法，跳转到 teamnoticeView的teamnoticexiangqing方法
    url(r'^teamnoticexiangqing/(?P<id>[0-9]+)$', teamnoticeViews.teamnoticexiangqing, name='teamnoticexiangqing'),
]
