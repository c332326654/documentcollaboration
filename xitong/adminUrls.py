# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import adminViews

urlpatterns = [

    #  定义添加管理员的url地址响应方法，跳转到 adminView的tianjiaadmin方法
    url(r'^tianjiaadmin/$', adminViews.tianjiaadmin, name='tianjiaadmin'),

    #  定义处理添加管理员的url地址响应方法，跳转到 adminView的tianjiaadminact方法
    url(r'^tianjiaadminact/$', adminViews.tianjiaadminact, name='tianjiaadminact'),

    #  定义跳转修改管理员的url地址响应方法，跳转到 adminView的xiugaiadmin方法
    url(r'^xiugaiadmin/(?P<id>[0-9]+)$', adminViews.xiugaiadmin, name='xiugaiadmin'),

    #  定义处理修改管理员的url地址响应方法，跳转到 adminView的xiugaiadminat方法
    url(r'^xiugaiadminact/$', adminViews.xiugaiadminact, name='xiugaiadminact'),

    #  定义跳转管理管理员的url地址响应方法，跳转到 adminView的adminguanli方法
    url(r'^adminguanli/$', adminViews.adminguanli, name='adminguanli'),

    #  定义跳转查看管理员的url地址响应方法，跳转到 adminView的adminchakan方法
    url(r'^adminchakan/$', adminViews.adminchakan, name='adminchakan'),

    #  定义处理删除管理员的url地址响应方法，跳转到 adminView的shanchuadmin方法
    url(r'^shanchuadminact/(?P<id>[0-9]+)$', adminViews.shanchuadminact, name='shanchuadminact'),

    #  定义跳转搜索管理员的url地址响应方法，跳转到 adminView的sousuoadmin方法
    url(r'^sousuoadmin/$', adminViews.sousuoadmin, name='sousuoadmin'),

    #  定义管理员详情的url地址响应方法，跳转到 adminView的adminxiangqing方法
    url(r'^adminxiangqing/(?P<id>[0-9]+)$', adminViews.adminxiangqing, name='adminxiangqing'),
]
