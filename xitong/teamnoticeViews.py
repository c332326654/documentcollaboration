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


#    定义添加团队公告的方法，响应页面请求
def tianjiateamnotice(request):
    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加团队公告页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiateamnotice.html', {'teamall': teamall, });


#  处理添加团队公告方法   
def tianjiateamnoticeact(request):
    #  从页面post数据中获取标题
    titlestr = request.POST.get("title");
    title = "";
    if (titlestr is not None):
        title = titlestr;

    #  从页面post数据中获取发布时间
    addtimestr = request.POST.get("addtime");
    addtime = "";
    if (addtimestr is not None):
        addtime = addtimestr;

    #  从页面post数据中获取内容
    contentstr = request.POST.get("content");
    content = "";
    if (contentstr is not None):
        content = contentstr;

    #  从页面post数据中获取团队
    teamstr = request.POST.get("team");
    team = "";
    if (teamstr is not None):
        team = teamstr;

    #  从页面post数据中获取团队id
    teamidstr = request.POST.get("teamid");
    teamid = "";
    if (teamidstr is not None):
        teamid = teamidstr;

    #  将团队公告的属性赋值给团队公告，生成团队公告对象
    teamnotice = models.Teamnotice(title=title, addtime=addtime, content=content, team=team, teamid=teamid, );

    #  调用save方法保存团队公告信息
    teamnotice.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加团队公告成功,并跳转到团队公告管理页面
    return HttpResponse(u"<p>添加团队公告成功</p><a href='/teamnotice/teamnoticeguanli'>返回页面</a>");


#  定义表名管理方法，响应页面teamnoticeguanli请求   
def teamnoticeguanli(request):

    searchCondition = {};

    teamid = request.GET.get("teamid");
    if (teamid is not None):
        searchCondition["teamid"] = teamid;


    #  通过all方法查询所有的团队公告信息
    teamnoticeall = models.Teamnotice.objects.filter(**searchCondition).all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队公告管理页面，并附带所有团队公告信息
    return render(request, 'xitong/teamnoticeguanli.html', {'teamnoticeall': teamnoticeall});


#  定义表名查看方法，响应页面teamnoticechakan请求   
def teamnoticechakan(request):

    #  通过all方法查询所有的团队公告信息
    teamnoticeall = models.Teamnotice.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队公告查看页面，并附带所有团队公告信息
    return render(request, 'xitong/teamnoticechakan.html', {'teamnoticeall': teamnoticeall});


#  定义修改团队公告方法，通过id查询对应的团队公告信息，返回页面展示  
def xiugaiteamnotice(request, id):
    #  使用get方法，通过id查询对应的团队公告信息
    teamnotice = models.Teamnotice.objects.get(id=id);

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  跳转到修改团队公告页面，并附带当前团队公告信息
    return render(request, 'xitong/xiugaiteamnotice.html', {'teamnotice': teamnotice, 'teamall': teamall, });


#  定义处理修改团队公告方法   
def xiugaiteamnoticeact(request):
    #  使用request获取post中的团队公告id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的团队公告id获取对应的团队公告信息
    teamnotice = models.Teamnotice.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给teamnotice的title字段
    titlestr = request.POST.get("title");
    if (titlestr is not None):
        teamnotice.title = titlestr;

    #  从页面post数据中获取发布时间并赋值给teamnotice的addtime字段
    addtimestr = request.POST.get("addtime");
    if (addtimestr is not None):
        teamnotice.addtime = addtimestr;

    #  从页面post数据中获取内容并赋值给teamnotice的content字段
    contentstr = request.POST.get("content");
    if (contentstr is not None):
        teamnotice.content = contentstr;

    #  从页面post数据中获取团队并赋值给teamnotice的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        teamnotice.team = teamstr;

    #  从页面post数据中获取团队id并赋值给teamnotice的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        teamnotice.teamid = teamidstr;

    #  调用save方法保存团队公告信息
    teamnotice.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改团队公告成功,并跳转到团队公告管理页面
    return HttpResponse(u"<p>修改团队公告成功</p><a href='/teamnotice/teamnoticeguanli'>返回页面</a>");


#  定义删除团队公告方法   
def shanchuteamnoticeact(request, id):
    #  调用django的delete方法，根据id删除团队公告信息
    models.Teamnotice.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除团队公告成功,并跳转到团队公告管理页面
    return HttpResponse(u"<p>删除团队公告成功</p><a href='/teamnotice/teamnoticeguanli'>返回页面</a>");


#  定义搜索团队公告方法，响应页面搜索请求   
def sousuoteamnotice(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的团队公告信息
    teamnoticeall = models.Teamnotice.objects.filter(title__icontains=search);

    #  跳转到搜索团队公告页面，并附带查询的团队公告信息
    return render(request, 'xitong/sousuoteamnotice.html', {"teamnoticeall": teamnoticeall});


#  处理团队公告详情   
def teamnoticexiangqing(request, id):
    #  根据页面传入id获取团队公告信息
    teamnotice = models.Teamnotice.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队公告详情页面,并团队公告信息传递到页面中
    return render(request, 'xitong/teamnoticexiangqing.html', {"teamnotice": teamnotice});
