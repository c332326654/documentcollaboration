# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import chatViews

urlpatterns = [

    #  定义添加聊天室的url地址响应方法，跳转到 chatView的tianjiachat方法
    url(r'^tianjiachat/$', chatViews.tianjiachat, name='tianjiachat'),

    #  定义处理添加聊天室的url地址响应方法，跳转到 chatView的tianjiachatact方法
    url(r'^tianjiachatact/$', chatViews.tianjiachatact, name='tianjiachatact'),

    #  定义跳转修改聊天室的url地址响应方法，跳转到 chatView的xiugaichat方法
    url(r'^xiugaichat/(?P<id>[0-9]+)$', chatViews.xiugaichat, name='xiugaichat'),

    #  定义处理修改聊天室的url地址响应方法，跳转到 chatView的xiugaichatat方法
    url(r'^xiugaichatact/$', chatViews.xiugaichatact, name='xiugaichatact'),

    #  定义跳转管理聊天室的url地址响应方法，跳转到 chatView的chatguanli方法
    url(r'^chatguanli/$', chatViews.chatguanli, name='chatguanli'),

    #  定义跳转查看聊天室的url地址响应方法，跳转到 chatView的chatchakan方法
    url(r'^chatchakan/$', chatViews.chatchakan, name='chatchakan'),

    #  定义处理删除聊天室的url地址响应方法，跳转到 chatView的shanchuchat方法
    url(r'^shanchuchatact/(?P<id>[0-9]+)$', chatViews.shanchuchatact, name='shanchuchatact'),

    #  定义跳转搜索聊天室的url地址响应方法，跳转到 chatView的sousuochat方法
    url(r'^sousuochat/$', chatViews.sousuochat, name='sousuochat'),

    #  定义聊天室详情的url地址响应方法，跳转到 chatView的chatxiangqing方法
    url(r'^chatxiangqing/(?P<id>[0-9]+)$', chatViews.chatxiangqing, name='chatxiangqing'),

    #  定义添加聊天室方法，响应页面请求，跳转到chatViews的usertianjiachat方法
    url(r'^usertianjiachat/$', chatViews.usertianjiachat, name='usertianjiachat'),

    #  定义处理添加聊天室方法，响应页面请求，跳转到chatViews的usertianjiachatact方法
    url(r'^usertianjiachatact/$', chatViews.usertianjiachatact, name='usertianjiachatact'),

    #  定义跳转修改聊天室方法，响应页面请求，跳转到chatViews的userxiugaichat方法
    url(r'^userxiugaichat/(?P<id>[0-9]+)$', chatViews.userxiugaichat, name='userxiugaichat'),

    #  定义处理修改聊天室方法，响应页面请求，跳转到chatViews的userxiugaichatact方法
    url(r'^userxiugaichatact/$', chatViews.userxiugaichatact, name='userxiugaichatact'),

    #  定义跳转聊天室管理方法，响应页面请求，跳转到chatViews的userchatguanli方法
    url(r'^userchatguanli/$', chatViews.userchatguanli, name='userchatguanli'),

    #  定义处理删除聊天室方法，响应页面请求，跳转到chatViews的usershanchuchat方法
    url(r'^usershanchuchatact/(?P<id>[0-9]+)$', chatViews.usershanchuchatact, name='usershanchuchatact'),
]
