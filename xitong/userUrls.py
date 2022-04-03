# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import userViews

urlpatterns = [

    #  定义添加用户的url地址响应方法，跳转到 userView的tianjiauser方法
    url(r'^tianjiauser/$', userViews.tianjiauser, name='tianjiauser'),

    #  定义处理添加用户的url地址响应方法，跳转到 userView的tianjiauseract方法
    url(r'^tianjiauseract/$', userViews.tianjiauseract, name='tianjiauseract'),

    #  定义跳转修改用户的url地址响应方法，跳转到 userView的xiugaiuser方法
    url(r'^xiugaiuser/(?P<id>[0-9]+)$', userViews.xiugaiuser, name='xiugaiuser'),

    #  定义处理修改用户的url地址响应方法，跳转到 userView的xiugaiuserat方法
    url(r'^xiugaiuseract/$', userViews.xiugaiuseract, name='xiugaiuseract'),

    #  定义跳转管理用户的url地址响应方法，跳转到 userView的userguanli方法
    url(r'^userguanli/$', userViews.userguanli, name='userguanli'),

    #  定义跳转查看用户的url地址响应方法，跳转到 userView的userchakan方法
    url(r'^userchakan/$', userViews.userchakan, name='userchakan'),

    #  定义处理删除用户的url地址响应方法，跳转到 userView的shanchuuser方法
    url(r'^shanchuuseract/(?P<id>[0-9]+)$', userViews.shanchuuseract, name='shanchuuseract'),

    #  定义跳转搜索用户的url地址响应方法，跳转到 userView的sousuouser方法
    url(r'^sousuouser/$', userViews.sousuouser, name='sousuouser'),

    #  定义用户详情的url地址响应方法，跳转到 userView的userxiangqing方法
    url(r'^userxiangqing/(?P<id>[0-9]+)$', userViews.userxiangqing, name='userxiangqing'),
]
