# coding:utf-8
from django.shortcuts import render
from json import dumps
from pprint import pprint
import math
import time
# Create your views here.
from django.http import HttpResponse
from . import models
import random, os;


#  定义上传文件方法
def uploadFile(request, filename):
    #  获取传入的文件信息
    file_obj = request.FILES.get(filename)

    #  如果传入的文件为空，则返回false
    if file_obj == None:
        return "false"

    #  获取该文件的后缀信息
    houzhui = file_obj.name.split(".")[-1];
    # 写入文件
    file_name = 'temp_file-%d' % random.randint(0, 100000) + "." + houzhui  # 不能使用文件名称，因为存在中文，会引起内部错误
    file_full_path = os.path.join("static/upload/", file_name)
    dest = open(file_full_path, 'wb+')
    dest.write(file_obj.read())
    dest.close()

    #  返回文件的名字
    return file_name;


#    定义添加管理员的方法，响应页面请求
def tianjiaadmin(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加管理员页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiaadmin.html', {});


#  处理添加管理员方法   
def tianjiaadminact(request):
    #  从页面post数据中获取账号
    usernamestr = request.POST.get("username");
    username = "";
    if (usernamestr is not None):
        username = usernamestr;

    #  从页面post数据中获取密码
    passwordstr = request.POST.get("password");
    password = "";
    if (passwordstr is not None):
        password = passwordstr;

    #  将管理员的属性赋值给管理员，生成管理员对象
    admin = models.Admin(username=username, password=password, );

    #  调用save方法保存管理员信息
    admin.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加管理员成功,并跳转到管理员管理页面
    return HttpResponse(u"<p>添加管理员成功</p><a href='/admin/adminguanli'>返回页面</a>");


#  定义表名管理方法，响应页面adminguanli请求   
def adminguanli(request):
    #  通过all方法查询所有的管理员信息
    adminall = models.Admin.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到管理员管理页面，并附带所有管理员信息
    return render(request, 'xitong/adminguanli.html', {'adminall': adminall});


#  定义表名查看方法，响应页面adminchakan请求   
def adminchakan(request):
    #  通过all方法查询所有的管理员信息
    adminall = models.Admin.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到管理员查看页面，并附带所有管理员信息
    return render(request, 'xitong/adminchakan.html', {'adminall': adminall});


#  定义修改管理员方法，通过id查询对应的管理员信息，返回页面展示  
def xiugaiadmin(request, id):
    #  使用get方法，通过id查询对应的管理员信息
    admin = models.Admin.objects.get(id=id);

    #  跳转到修改管理员页面，并附带当前管理员信息
    return render(request, 'xitong/xiugaiadmin.html', {'admin': admin, });


#  定义处理修改管理员方法   
def xiugaiadminact(request):
    #  使用request获取post中的管理员id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的管理员id获取对应的管理员信息
    admin = models.Admin.objects.get(id=id);

    #  从页面post数据中获取账号并赋值给admin的username字段
    usernamestr = request.POST.get("username");
    if (usernamestr is not None):
        admin.username = usernamestr;

    #  从页面post数据中获取密码并赋值给admin的password字段
    passwordstr = request.POST.get("password");
    if (passwordstr is not None):
        admin.password = passwordstr;

    #  调用save方法保存管理员信息
    admin.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改管理员成功,并跳转到管理员管理页面
    return HttpResponse(u"<p>修改管理员成功</p><a href='/admin/adminguanli'>返回页面</a>");


#  定义删除管理员方法   
def shanchuadminact(request, id):
    #  调用django的delete方法，根据id删除管理员信息
    models.Admin.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除管理员成功,并跳转到管理员管理页面
    return HttpResponse(u"<p>删除管理员成功</p><a href='/admin/adminguanli'>返回页面</a>");


#  定义搜索管理员方法，响应页面搜索请求   
def sousuoadmin(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的管理员信息
    adminall = models.Admin.objects.filter(username__icontains=search);

    #  跳转到搜索管理员页面，并附带查询的管理员信息
    return render(request, 'xitong/sousuoadmin.html', {"adminall": adminall});


#  处理管理员详情   
def adminxiangqing(request, id):
    #  根据页面传入id获取管理员信息
    admin = models.Admin.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到管理员详情页面,并管理员信息传递到页面中
    return render(request, 'xitong/adminxiangqing.html', {"admin": admin});
