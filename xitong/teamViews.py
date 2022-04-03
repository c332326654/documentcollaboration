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


#    定义添加团队的方法，响应页面请求
def tianjiateam(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加团队页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiateam.html', {'userall': userall, });


#  处理添加团队方法   
def tianjiateamact(request):
    #  从页面post数据中获取名称
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取负责人
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取负责人id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取介绍
    introducestr = request.POST.get("introduce");
    introduce = "";
    if (introducestr is not None):
        introduce = introducestr;

    #  将团队的属性赋值给团队，生成团队对象
    team = models.Team(name=name, user=user, userid=userid, introduce=introduce, );

    #  调用save方法保存团队信息
    team.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加团队成功,并跳转到团队管理页面
    return HttpResponse(u"<p>添加团队成功</p><a href='/team/teamguanli'>返回页面</a>");


#  定义表名管理方法，响应页面teamguanli请求   
def teamguanli(request):
    #  通过all方法查询所有的团队信息
    teamall = models.Team.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队管理页面，并附带所有团队信息
    return render(request, 'xitong/teamguanli.html', {'teamall': teamall});


#  定义表名查看方法，响应页面teamchakan请求   
def teamchakan(request):
    #  通过all方法查询所有的团队信息
    teamall = models.Team.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队查看页面，并附带所有团队信息
    return render(request, 'xitong/teamchakan.html', {'teamall': teamall});


#  定义修改团队方法，通过id查询对应的团队信息，返回页面展示  
def xiugaiteam(request, id):
    #  使用get方法，通过id查询对应的团队信息
    team = models.Team.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改团队页面，并附带当前团队信息
    return render(request, 'xitong/xiugaiteam.html', {'team': team, 'userall': userall, });


#  定义处理修改团队方法   
def xiugaiteamact(request):
    #  使用request获取post中的团队id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的团队id获取对应的团队信息
    team = models.Team.objects.get(id=id);

    #  从页面post数据中获取名称并赋值给team的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        team.name = namestr;

    #  从页面post数据中获取负责人并赋值给team的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        team.user = userstr;

    #  从页面post数据中获取负责人id并赋值给team的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        team.userid = useridstr;

    #  从页面post数据中获取介绍并赋值给team的introduce字段
    introducestr = request.POST.get("introduce");
    if (introducestr is not None):
        team.introduce = introducestr;

    #  调用save方法保存团队信息
    team.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改团队成功,并跳转到团队管理页面
    return HttpResponse(u"<p>修改团队成功</p><a href='/team/teamguanli'>返回页面</a>");


#  定义删除团队方法   
def shanchuteamact(request, id):
    #  调用django的delete方法，根据id删除团队信息
    models.Team.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除团队成功,并跳转到团队管理页面
    return HttpResponse(u"<p>删除团队成功</p><a href='/team/teamguanli'>返回页面</a>");


#  定义搜索团队方法，响应页面搜索请求   
def sousuoteam(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的团队信息
    teamall = models.Team.objects.filter(name__icontains=search);

    #  跳转到搜索团队页面，并附带查询的团队信息
    return render(request, 'xitong/sousuoteam.html', {"teamall": teamall});


#  处理团队详情   
def teamxiangqing(request, id):
    #  根据页面传入id获取团队信息
    team = models.Team.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队详情页面,并团队信息传递到页面中
    return render(request, 'xitong/teamxiangqing.html', {"team": team});


#  定义跳转user添加团队页面的方法  
def usertianjiateam(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加团队页面
    return render(request, 'xitong/usertianjiateam.html', {'userall': userall, });


#  处理添加团队方法   
def usertianjiateamact(request):
    #  从页面post数据中获取名称
    namestr = request.POST.get("name");
    name = "";
    if (namestr is not None):
        name = namestr;

    #  从页面post数据中获取负责人
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取负责人id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取介绍
    introducestr = request.POST.get("introduce");
    introduce = "";
    if (introducestr is not None):
        introduce = introducestr;

    #  将团队的属性赋值给团队，生成团队对象
    team = models.Team(name=name, user=user, userid=userid, introduce=introduce, );

    #  调用save方法保存团队信息
    team.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加团队成功,并跳转到团队管理页面
    return HttpResponse(u"<p>添加团队成功</p><a href='/team/userteamguanli'>返回页面</a>");


#  跳转user团队管理页面
def userteamguanli(request):
    #  查询出userid等于当前用户id的所有团队信息
    teamall = models.Team.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回团队管理页面，并携带teamall的数据信息
    return render(request, 'xitong/userteamguanli.html', {'teamall': teamall});


#  定义跳转user修改团队页面      
def userxiugaiteam(request, id):
    #  根据页面传入的团队id信息，查询出对应的团队信息
    team = models.Team.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改团队页面，并携带查询出的团队信息
    return render(request, 'xitong/userxiugaiteam.html', {'team': team, 'userall': userall, });


#  定义处理修改团队方法   
def userxiugaiteamact(request):
    #  使用request获取post中的团队id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的团队id获取对应的团队信息
    team = models.Team.objects.get(id=id);

    #  从页面post数据中获取名称并赋值给team的name字段
    namestr = request.POST.get("name");
    if (namestr is not None):
        team.name = namestr;

    #  从页面post数据中获取负责人并赋值给team的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        team.user = userstr;

    #  从页面post数据中获取负责人id并赋值给team的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        team.userid = useridstr;

    #  从页面post数据中获取介绍并赋值给team的introduce字段
    introducestr = request.POST.get("introduce");
    if (introducestr is not None):
        team.introduce = introducestr;

    #  调用save方法保存团队信息
    team.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改团队成功,并跳转到团队管理页面
    return HttpResponse(u"<p>修改团队成功</p><a href='/team/userteamguanli'>返回页面</a>");


#  定义user删除团队信息
def usershanchuteamact(request, id):
    #  根据页面传入的团队id信息，删除出对应的团队信息
    models.Team.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除团队成功，并跳转到团队管理页面
    return HttpResponse(u"<p>删除团队成功</p><a href='/team/userteamguanli'>返回页面</a>");
