# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import teamViews

urlpatterns = [

    #  定义添加团队的url地址响应方法，跳转到 teamView的tianjiateam方法
    url(r'^tianjiateam/$', teamViews.tianjiateam, name='tianjiateam'),

    #  定义处理添加团队的url地址响应方法，跳转到 teamView的tianjiateamact方法
    url(r'^tianjiateamact/$', teamViews.tianjiateamact, name='tianjiateamact'),

    #  定义跳转修改团队的url地址响应方法，跳转到 teamView的xiugaiteam方法
    url(r'^xiugaiteam/(?P<id>[0-9]+)$', teamViews.xiugaiteam, name='xiugaiteam'),

    #  定义处理修改团队的url地址响应方法，跳转到 teamView的xiugaiteamat方法
    url(r'^xiugaiteamact/$', teamViews.xiugaiteamact, name='xiugaiteamact'),

    #  定义跳转管理团队的url地址响应方法，跳转到 teamView的teamguanli方法
    url(r'^teamguanli/$', teamViews.teamguanli, name='teamguanli'),

    #  定义跳转查看团队的url地址响应方法，跳转到 teamView的teamchakan方法
    url(r'^teamchakan/$', teamViews.teamchakan, name='teamchakan'),

    #  定义处理删除团队的url地址响应方法，跳转到 teamView的shanchuteam方法
    url(r'^shanchuteamact/(?P<id>[0-9]+)$', teamViews.shanchuteamact, name='shanchuteamact'),

    #  定义跳转搜索团队的url地址响应方法，跳转到 teamView的sousuoteam方法
    url(r'^sousuoteam/$', teamViews.sousuoteam, name='sousuoteam'),

    #  定义团队详情的url地址响应方法，跳转到 teamView的teamxiangqing方法
    url(r'^teamxiangqing/(?P<id>[0-9]+)$', teamViews.teamxiangqing, name='teamxiangqing'),

    #  定义添加团队方法，响应页面请求，跳转到teamViews的usertianjiateam方法
    url(r'^usertianjiateam/$', teamViews.usertianjiateam, name='usertianjiateam'),

    #  定义处理添加团队方法，响应页面请求，跳转到teamViews的usertianjiateamact方法
    url(r'^usertianjiateamact/$', teamViews.usertianjiateamact, name='usertianjiateamact'),

    #  定义跳转修改团队方法，响应页面请求，跳转到teamViews的userxiugaiteam方法
    url(r'^userxiugaiteam/(?P<id>[0-9]+)$', teamViews.userxiugaiteam, name='userxiugaiteam'),

    #  定义处理修改团队方法，响应页面请求，跳转到teamViews的userxiugaiteamact方法
    url(r'^userxiugaiteamact/$', teamViews.userxiugaiteamact, name='userxiugaiteamact'),

    #  定义跳转团队管理方法，响应页面请求，跳转到teamViews的userteamguanli方法
    url(r'^userteamguanli/$', teamViews.userteamguanli, name='userteamguanli'),

    #  定义处理删除团队方法，响应页面请求，跳转到teamViews的usershanchuteam方法
    url(r'^usershanchuteamact/(?P<id>[0-9]+)$', teamViews.usershanchuteamact, name='usershanchuteamact'),
]
