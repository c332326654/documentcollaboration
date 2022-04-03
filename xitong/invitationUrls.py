# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import invitationViews

urlpatterns = [

    #  定义添加邀请的url地址响应方法，跳转到 invitationView的tianjiainvitation方法
    url(r'^tianjiainvitation/$', invitationViews.tianjiainvitation, name='tianjiainvitation'),

    #  定义处理添加邀请的url地址响应方法，跳转到 invitationView的tianjiainvitationact方法
    url(r'^tianjiainvitationact/$', invitationViews.tianjiainvitationact, name='tianjiainvitationact'),

    #  定义跳转修改邀请的url地址响应方法，跳转到 invitationView的xiugaiinvitation方法
    url(r'^xiugaiinvitation/(?P<id>[0-9]+)$', invitationViews.xiugaiinvitation, name='xiugaiinvitation'),

    #  定义处理修改邀请的url地址响应方法，跳转到 invitationView的xiugaiinvitationat方法
    url(r'^xiugaiinvitationact/$', invitationViews.xiugaiinvitationact, name='xiugaiinvitationact'),

    #  定义跳转管理邀请的url地址响应方法，跳转到 invitationView的invitationguanli方法
    url(r'^invitationguanli/$', invitationViews.invitationguanli, name='invitationguanli'),

    #  定义跳转查看邀请的url地址响应方法，跳转到 invitationView的invitationchakan方法
    url(r'^invitationchakan/$', invitationViews.invitationchakan, name='invitationchakan'),

    #  定义处理删除邀请的url地址响应方法，跳转到 invitationView的shanchuinvitation方法
    url(r'^shanchuinvitationact/(?P<id>[0-9]+)$', invitationViews.shanchuinvitationact, name='shanchuinvitationact'),

    #  定义跳转搜索邀请的url地址响应方法，跳转到 invitationView的sousuoinvitation方法
    url(r'^sousuoinvitation/$', invitationViews.sousuoinvitation, name='sousuoinvitation'),

    #  定义邀请详情的url地址响应方法，跳转到 invitationView的invitationxiangqing方法
    url(r'^invitationxiangqing/(?P<id>[0-9]+)$', invitationViews.invitationxiangqing, name='invitationxiangqing'),

    #  定义添加邀请方法，响应页面请求，跳转到invitationViews的usertianjiainvitation方法
    url(r'^usertianjiainvitation/$', invitationViews.usertianjiainvitation, name='usertianjiainvitation'),

    #  定义处理添加邀请方法，响应页面请求，跳转到invitationViews的usertianjiainvitationact方法
    url(r'^usertianjiainvitationact/$', invitationViews.usertianjiainvitationact, name='usertianjiainvitationact'),

    #  定义跳转修改邀请方法，响应页面请求，跳转到invitationViews的userxiugaiinvitation方法
    url(r'^userxiugaiinvitation/(?P<id>[0-9]+)$', invitationViews.userxiugaiinvitation, name='userxiugaiinvitation'),
    url(r'^usertongyiinvitation/(?P<id>[0-9]+)$', invitationViews.usertongyiinvitation, name='usertongyiinvitation'),
    url(r'^userjujueinvitation/(?P<id>[0-9]+)$', invitationViews.userjujueinvitation, name='userjujueinvitation'),

    #  定义处理修改邀请方法，响应页面请求，跳转到invitationViews的userxiugaiinvitationact方法
    url(r'^userxiugaiinvitationact/$', invitationViews.userxiugaiinvitationact, name='userxiugaiinvitationact'),

    #  定义跳转邀请管理方法，响应页面请求，跳转到invitationViews的userinvitationguanli方法
    url(r'^userinvitationguanli/$', invitationViews.userinvitationguanli, name='userinvitationguanli'),

    #  定义处理删除邀请方法，响应页面请求，跳转到invitationViews的usershanchuinvitation方法
    url(r'^usershanchuinvitationact/(?P<id>[0-9]+)$', invitationViews.usershanchuinvitationact,
        name='usershanchuinvitationact'),
]
