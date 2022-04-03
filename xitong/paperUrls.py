# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import paperViews

urlpatterns = [

    #  定义添加论文的url地址响应方法，跳转到 paperView的tianjiapaper方法
    url(r'^tianjiapaper/$', paperViews.tianjiapaper, name='tianjiapaper'),

    #  定义处理添加论文的url地址响应方法，跳转到 paperView的tianjiapaperact方法
    url(r'^tianjiapaperact/$', paperViews.tianjiapaperact, name='tianjiapaperact'),

    #  定义跳转修改论文的url地址响应方法，跳转到 paperView的xiugaipaper方法
    url(r'^xiugaipaper/(?P<id>[0-9]+)$', paperViews.xiugaipaper, name='xiugaipaper'),

    #  定义处理修改论文的url地址响应方法，跳转到 paperView的xiugaipaperat方法
    url(r'^xiugaipaperact/$', paperViews.xiugaipaperact, name='xiugaipaperact'),

    #  定义跳转管理论文的url地址响应方法，跳转到 paperView的paperguanli方法
    url(r'^paperguanli/$', paperViews.paperguanli, name='paperguanli'),

    #  定义跳转查看论文的url地址响应方法，跳转到 paperView的paperchakan方法
    url(r'^paperchakan/$', paperViews.paperchakan, name='paperchakan'),
    url(r'^papertuijian/$', paperViews.papertuijian, name='papertuijian'),

    #  定义处理删除论文的url地址响应方法，跳转到 paperView的shanchupaper方法
    url(r'^shanchupaperact/(?P<id>[0-9]+)$', paperViews.shanchupaperact, name='shanchupaperact'),

    #  定义跳转搜索论文的url地址响应方法，跳转到 paperView的sousuopaper方法
    url(r'^sousuopaper/$', paperViews.sousuopaper, name='sousuopaper'),

    #  定义论文详情的url地址响应方法，跳转到 paperView的paperxiangqing方法
    url(r'^paperxiangqing/(?P<id>[0-9]+)$', paperViews.paperxiangqing, name='paperxiangqing'),

    #  定义添加论文方法，响应页面请求，跳转到paperViews的usertianjiapaper方法
    url(r'^usertianjiapaper/$', paperViews.usertianjiapaper, name='usertianjiapaper'),

    #  定义处理添加论文方法，响应页面请求，跳转到paperViews的usertianjiapaperact方法
    url(r'^usertianjiapaperact/$', paperViews.usertianjiapaperact, name='usertianjiapaperact'),

    #  定义跳转修改论文方法，响应页面请求，跳转到paperViews的userxiugaipaper方法
    url(r'^userxiugaipaper/(?P<id>[0-9]+)$', paperViews.userxiugaipaper, name='userxiugaipaper'),

    #  定义处理修改论文方法，响应页面请求，跳转到paperViews的userxiugaipaperact方法
    url(r'^userxiugaipaperact/$', paperViews.userxiugaipaperact, name='userxiugaipaperact'),

    #  定义跳转论文管理方法，响应页面请求，跳转到paperViews的userpaperguanli方法
    url(r'^userpaperguanli/$', paperViews.userpaperguanli, name='userpaperguanli'),

    #  定义处理删除论文方法，响应页面请求，跳转到paperViews的usershanchupaper方法
    url(r'^usershanchupaperact/(?P<id>[0-9]+)$', paperViews.usershanchupaperact, name='usershanchupaperact'),
]
