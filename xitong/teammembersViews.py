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


#    定义添加团队成员的方法，响应页面请求
def tianjiateammembers(request):
    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加团队成员页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiateammembers.html', {'teamall': teamall, 'userall': userall, });


#  处理添加团队成员方法   
def tianjiateammembersact(request):
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

    #  从页面post数据中获取成员名字
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取成员id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  将团队成员的属性赋值给团队成员，生成团队成员对象
    teammembers = models.Teammembers(team=team, teamid=teamid, user=user, userid=userid, );

    #  调用save方法保存团队成员信息
    teammembers.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加团队成员成功,并跳转到团队成员管理页面
    return HttpResponse(u"<p>添加团队成员成功</p><a href='/teammembers/teammembersguanli'>返回页面</a>");


#  定义表名管理方法，响应页面teammembersguanli请求   
def teammembersguanli(request):
    #  通过all方法查询所有的团队成员信息
    teammembersall = models.Teammembers.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队成员管理页面，并附带所有团队成员信息
    return render(request, 'xitong/teammembersguanli.html', {'teammembersall': teammembersall});


#  定义表名查看方法，响应页面teammemberschakan请求   
def teammemberschakan(request):
    #  通过all方法查询所有的团队成员信息
    teammembersall = models.Teammembers.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队成员查看页面，并附带所有团队成员信息
    return render(request, 'xitong/teammemberschakan.html', {'teammembersall': teammembersall});


#  定义修改团队成员方法，通过id查询对应的团队成员信息，返回页面展示  
def xiugaiteammembers(request, id):
    #  使用get方法，通过id查询对应的团队成员信息
    teammembers = models.Teammembers.objects.get(id=id);

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改团队成员页面，并附带当前团队成员信息
    return render(request, 'xitong/xiugaiteammembers.html',
                  {'teammembers': teammembers, 'teamall': teamall, 'userall': userall, });


#  定义处理修改团队成员方法   
def xiugaiteammembersact(request):
    #  使用request获取post中的团队成员id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的团队成员id获取对应的团队成员信息
    teammembers = models.Teammembers.objects.get(id=id);

    #  从页面post数据中获取团队并赋值给teammembers的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        teammembers.team = teamstr;

    #  从页面post数据中获取团队id并赋值给teammembers的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        teammembers.teamid = teamidstr;

    #  从页面post数据中获取成员名字并赋值给teammembers的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        teammembers.user = userstr;

    #  从页面post数据中获取成员id并赋值给teammembers的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        teammembers.userid = useridstr;

    #  调用save方法保存团队成员信息
    teammembers.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改团队成员成功,并跳转到团队成员管理页面
    return HttpResponse(u"<p>修改团队成员成功</p><a href='/teammembers/teammembersguanli'>返回页面</a>");


#  定义删除团队成员方法   
def shanchuteammembersact(request, id):
    #  调用django的delete方法，根据id删除团队成员信息
    models.Teammembers.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除团队成员成功,并跳转到团队成员管理页面
    return HttpResponse(u"<p>删除团队成员成功</p><a href='/teammembers/teammembersguanli'>返回页面</a>");


#  定义搜索团队成员方法，响应页面搜索请求   
def sousuoteammembers(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的团队成员信息
    teammembersall = models.Teammembers.objects.filter(team__icontains=search);

    #  跳转到搜索团队成员页面，并附带查询的团队成员信息
    return render(request, 'xitong/sousuoteammembers.html', {"teammembersall": teammembersall});


#  处理团队成员详情   
def teammembersxiangqing(request, id):
    #  根据页面传入id获取团队成员信息
    teammembers = models.Teammembers.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到团队成员详情页面,并团队成员信息传递到页面中
    return render(request, 'xitong/teammembersxiangqing.html', {"teammembers": teammembers});


#  定义跳转user添加团队成员页面的方法  
def usertianjiateammembers(request):
    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加团队成员页面
    return render(request, 'xitong/usertianjiateammembers.html', {'teamall': teamall, 'userall': userall, });


#  处理添加团队成员方法   
def usertianjiateammembersact(request):
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

    #  从页面post数据中获取成员名字
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取成员id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  将团队成员的属性赋值给团队成员，生成团队成员对象
    teammembers = models.Teammembers(team=team, teamid=teamid, user=user, userid=userid, );

    #  调用save方法保存团队成员信息
    teammembers.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加团队成员成功,并跳转到团队成员管理页面
    return HttpResponse(u"<p>添加团队成员成功</p><a href='/teammembers/userteammembersguanli'>返回页面</a>");


#  跳转user团队成员管理页面
def userteammembersguanli(request):
    #  查询出userid等于当前用户id的所有团队成员信息
    teammembersall = models.Teammembers.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回团队成员管理页面，并携带teammembersall的数据信息
    return render(request, 'xitong/userteammembersguanli.html', {'teammembersall': teammembersall});


#  定义跳转user修改团队成员页面      
def userxiugaiteammembers(request, id):
    #  根据页面传入的团队成员id信息，查询出对应的团队成员信息
    teammembers = models.Teammembers.objects.get(id=id);

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改团队成员页面，并携带查询出的团队成员信息
    return render(request, 'xitong/userxiugaiteammembers.html',
                  {'teammembers': teammembers, 'teamall': teamall, 'userall': userall, });


#  定义处理修改团队成员方法   
def userxiugaiteammembersact(request):
    #  使用request获取post中的团队成员id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的团队成员id获取对应的团队成员信息
    teammembers = models.Teammembers.objects.get(id=id);

    #  从页面post数据中获取团队并赋值给teammembers的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        teammembers.team = teamstr;

    #  从页面post数据中获取团队id并赋值给teammembers的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        teammembers.teamid = teamidstr;

    #  从页面post数据中获取成员名字并赋值给teammembers的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        teammembers.user = userstr;

    #  从页面post数据中获取成员id并赋值给teammembers的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        teammembers.userid = useridstr;

    #  调用save方法保存团队成员信息
    teammembers.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改团队成员成功,并跳转到团队成员管理页面
    return HttpResponse(u"<p>修改团队成员成功</p><a href='/teammembers/userteammembersguanli'>返回页面</a>");


#  定义user删除团队成员信息
def usershanchuteammembersact(request, id):
    #  根据页面传入的团队成员id信息，删除出对应的团队成员信息
    models.Teammembers.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除团队成员成功，并跳转到团队成员管理页面
    return HttpResponse(u"<p>删除团队成员成功</p><a href='/teammembers/userteammembersguanli'>返回页面</a>");
