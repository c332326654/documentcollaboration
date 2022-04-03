# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import teammembersViews

urlpatterns = [

    #  定义添加团队成员的url地址响应方法，跳转到 teammembersView的tianjiateammembers方法
    url(r'^tianjiateammembers/$', teammembersViews.tianjiateammembers, name='tianjiateammembers'),

    #  定义处理添加团队成员的url地址响应方法，跳转到 teammembersView的tianjiateammembersact方法
    url(r'^tianjiateammembersact/$', teammembersViews.tianjiateammembersact, name='tianjiateammembersact'),

    #  定义跳转修改团队成员的url地址响应方法，跳转到 teammembersView的xiugaiteammembers方法
    url(r'^xiugaiteammembers/(?P<id>[0-9]+)$', teammembersViews.xiugaiteammembers, name='xiugaiteammembers'),

    #  定义处理修改团队成员的url地址响应方法，跳转到 teammembersView的xiugaiteammembersat方法
    url(r'^xiugaiteammembersact/$', teammembersViews.xiugaiteammembersact, name='xiugaiteammembersact'),

    #  定义跳转管理团队成员的url地址响应方法，跳转到 teammembersView的teammembersguanli方法
    url(r'^teammembersguanli/$', teammembersViews.teammembersguanli, name='teammembersguanli'),

    #  定义跳转查看团队成员的url地址响应方法，跳转到 teammembersView的teammemberschakan方法
    url(r'^teammemberschakan/$', teammembersViews.teammemberschakan, name='teammemberschakan'),

    #  定义处理删除团队成员的url地址响应方法，跳转到 teammembersView的shanchuteammembers方法
    url(r'^shanchuteammembersact/(?P<id>[0-9]+)$', teammembersViews.shanchuteammembersact,
        name='shanchuteammembersact'),

    #  定义跳转搜索团队成员的url地址响应方法，跳转到 teammembersView的sousuoteammembers方法
    url(r'^sousuoteammembers/$', teammembersViews.sousuoteammembers, name='sousuoteammembers'),

    #  定义团队成员详情的url地址响应方法，跳转到 teammembersView的teammembersxiangqing方法
    url(r'^teammembersxiangqing/(?P<id>[0-9]+)$', teammembersViews.teammembersxiangqing, name='teammembersxiangqing'),

    #  定义添加团队成员方法，响应页面请求，跳转到teammembersViews的usertianjiateammembers方法
    url(r'^usertianjiateammembers/$', teammembersViews.usertianjiateammembers, name='usertianjiateammembers'),

    #  定义处理添加团队成员方法，响应页面请求，跳转到teammembersViews的usertianjiateammembersact方法
    url(r'^usertianjiateammembersact/$', teammembersViews.usertianjiateammembersact, name='usertianjiateammembersact'),

    #  定义跳转修改团队成员方法，响应页面请求，跳转到teammembersViews的userxiugaiteammembers方法
    url(r'^userxiugaiteammembers/(?P<id>[0-9]+)$', teammembersViews.userxiugaiteammembers,
        name='userxiugaiteammembers'),

    #  定义处理修改团队成员方法，响应页面请求，跳转到teammembersViews的userxiugaiteammembersact方法
    url(r'^userxiugaiteammembersact/$', teammembersViews.userxiugaiteammembersact, name='userxiugaiteammembersact'),

    #  定义跳转团队成员管理方法，响应页面请求，跳转到teammembersViews的userteammembersguanli方法
    url(r'^userteammembersguanli/$', teammembersViews.userteammembersguanli, name='userteammembersguanli'),

    #  定义处理删除团队成员方法，响应页面请求，跳转到teammembersViews的usershanchuteammembers方法
    url(r'^usershanchuteammembersact/(?P<id>[0-9]+)$', teammembersViews.usershanchuteammembersact,
        name='usershanchuteammembersact'),
]
