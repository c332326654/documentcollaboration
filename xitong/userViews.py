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


#    定义添加用户的方法，响应页面请求
def tianjiauser(request):
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加用户页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiauser.html', {});


#  处理添加用户方法   
def tianjiauseract(request):
    #  从页面post数据中获取名字
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取真实姓名
    realnamestr = request.POST.get("realname");
    realname = "";
    if (realnamestr is not None):
        realname = realnamestr;

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

    #  从页面post数据中获取性别
    sexstr = request.POST.get("sex");
    sex = "";
    if (sexstr is not None):
        sex = sexstr;

    #  从页面post数据中获取性别
    agestr = request.POST.get("age");
    age = "";
    if (agestr is not None):
        age = agestr;

    #  从页面post数据中获取介绍
    introducestr = request.POST.get("introduce");
    introduce = "";
    if (introducestr is not None):
        introduce = introducestr;

    #  将用户的属性赋值给用户，生成用户对象
    user = models.User(name=name, realname=realname, username=username, password=password, sex=sex, age=age,
                       introduce=introduce, );

    #  调用save方法保存用户信息
    user.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加用户成功,并跳转到用户管理页面
    return HttpResponse(u"<p>添加用户成功</p><a href='/user/userguanli'>返回页面</a>");


#  定义表名管理方法，响应页面userguanli请求   
def userguanli(request):
    #  通过all方法查询所有的用户信息
    userall = models.User.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到用户管理页面，并附带所有用户信息
    return render(request, 'xitong/userguanli.html', {'userall': userall});


#  定义表名查看方法，响应页面userchakan请求   
def userchakan(request):
    #  通过all方法查询所有的用户信息
    userall = models.User.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到用户查看页面，并附带所有用户信息
    return render(request, 'xitong/userchakan.html', {'userall': userall});


#  定义修改用户方法，通过id查询对应的用户信息，返回页面展示  
def xiugaiuser(request, id):
    #  使用get方法，通过id查询对应的用户信息
    user = models.User.objects.get(id=id);

    #  跳转到修改用户页面，并附带当前用户信息
    return render(request, 'xitong/xiugaiuser.html', {'user': user, });


#  定义处理修改用户方法   
def xiugaiuseract(request):
    #  使用request获取post中的用户id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的用户id获取对应的用户信息
    user = models.User.objects.get(id=id);

    #  从页面post数据中获取名字并赋值给user的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        user.name = namestr;

    #  从页面post数据中获取真实姓名并赋值给user的realname字段
    realnamestr = request.POST.get("realname");
    if (realnamestr is not None):
        user.realname = realnamestr;

    #  从页面post数据中获取账号并赋值给user的username字段
    usernamestr = request.POST.get("username");
    if (usernamestr is not None):
        user.username = usernamestr;

    #  从页面post数据中获取密码并赋值给user的password字段
    passwordstr = request.POST.get("password");
    if (passwordstr is not None):
        user.password = passwordstr;

    #  从页面post数据中获取性别并赋值给user的sex字段
    sexstr = request.POST.get("sex");
    if (sexstr is not None):
        user.sex = sexstr;

    #  从页面post数据中获取性别并赋值给user的age字段
    agestr = request.POST.get("age");
    if (agestr is not None):
        user.age = agestr;

    #  从页面post数据中获取介绍并赋值给user的introduce字段
    introducestr = request.POST.get("introduce");
    if (introducestr is not None):
        user.introduce = introducestr;

    #  调用save方法保存用户信息
    user.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改用户成功,并跳转到用户管理页面
    return HttpResponse(u"<p>修改用户成功</p><a href='/user/userguanli'>返回页面</a>");


#  定义删除用户方法   
def shanchuuseract(request, id):
    #  调用django的delete方法，根据id删除用户信息
    models.User.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除用户成功,并跳转到用户管理页面
    return HttpResponse(u"<p>删除用户成功</p><a href='/user/userguanli'>返回页面</a>");


#  定义搜索用户方法，响应页面搜索请求   
def sousuouser(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的用户信息
    userall = models.User.objects.filter(name__icontains=search);

    #  跳转到搜索用户页面，并附带查询的用户信息
    return render(request, 'xitong/sousuouser.html', {"userall": userall});


#  处理用户详情   
def userxiangqing(request, id):
    #  根据页面传入id获取用户信息
    user = models.User.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到用户详情页面,并用户信息传递到页面中
    return render(request, 'xitong/userxiangqing.html', {"user": user});
