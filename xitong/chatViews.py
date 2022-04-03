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


#    定义添加聊天室的方法，响应页面请求
def tianjiachat(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加聊天室页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiachat.html', {'userall': userall, 'teamall': teamall, });


#  处理添加聊天室方法   
def tianjiachatact(request):
    #  从页面post数据中获取发信人
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取发信人id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取发言时间
    addtimestr = request.POST.get("addtime");
    addtime = "";
    if (addtimestr is not None):
        addtime = addtimestr;

    #  从页面post数据中获取发言内容
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

    #  将聊天室的属性赋值给聊天室，生成聊天室对象
    chat = models.Chat(user=user, userid=userid, addtime=addtime, content=content, team=team, teamid=teamid, );

    #  调用save方法保存聊天室信息
    chat.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加聊天室成功,并跳转到聊天室管理页面
    return HttpResponse(u"<p>添加聊天室成功</p><a href='/chat/chatguanli'>返回页面</a>");


#  定义表名管理方法，响应页面chatguanli请求   
def chatguanli(request):
    #  通过all方法查询所有的聊天室信息
    chatall = models.Chat.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到聊天室管理页面，并附带所有聊天室信息
    return render(request, 'xitong/chatguanli.html', {'chatall': chatall});


#  定义表名查看方法，响应页面chatchakan请求   
def chatchakan(request):

    searchCondition = {};

    teamid = request.GET.get("teamid");
    if (teamid is not None):
        searchCondition["teamid"] = teamid;

    teamitem = models.Team.objects.get(id=teamid);


    #  通过all方法查询所有的聊天室信息
    chatall = models.Chat.objects.filter(**searchCondition).all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到聊天室查看页面，并附带所有聊天室信息
    return render(request, 'xitong/chatchakan.html', {'chatall': chatall,"teamid":teamid,"team":teamitem.name});


#  定义修改聊天室方法，通过id查询对应的聊天室信息，返回页面展示  
def xiugaichat(request, id):
    #  使用get方法，通过id查询对应的聊天室信息
    chat = models.Chat.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  跳转到修改聊天室页面，并附带当前聊天室信息
    return render(request, 'xitong/xiugaichat.html', {'chat': chat, 'userall': userall, 'teamall': teamall, });


#  定义处理修改聊天室方法   
def xiugaichatact(request):
    #  使用request获取post中的聊天室id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的聊天室id获取对应的聊天室信息
    chat = models.Chat.objects.get(id=id);

    #  从页面post数据中获取发信人并赋值给chat的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        chat.user = userstr;

    #  从页面post数据中获取发信人id并赋值给chat的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        chat.userid = useridstr;

    #  从页面post数据中获取发言时间并赋值给chat的addtime字段
    addtimestr = request.POST.get("addtime");
    if (addtimestr is not None):
        chat.addtime = addtimestr;

    #  从页面post数据中获取发言内容并赋值给chat的content字段
    contentstr = request.POST.get("content");
    if (contentstr is not None):
        chat.content = contentstr;

    #  从页面post数据中获取团队并赋值给chat的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        chat.team = teamstr;

    #  从页面post数据中获取团队id并赋值给chat的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        chat.teamid = teamidstr;

    #  调用save方法保存聊天室信息
    chat.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改聊天室成功,并跳转到聊天室管理页面
    return HttpResponse(u"<p>修改聊天室成功</p><a href='/chat/chatguanli'>返回页面</a>");


#  定义删除聊天室方法   
def shanchuchatact(request, id):
    #  调用django的delete方法，根据id删除聊天室信息
    models.Chat.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除聊天室成功,并跳转到聊天室管理页面
    return HttpResponse(u"<p>删除聊天室成功</p><a href='/chat/chatguanli'>返回页面</a>");


#  定义搜索聊天室方法，响应页面搜索请求   
def sousuochat(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的聊天室信息
    chatall = models.Chat.objects.filter(user__icontains=search);

    #  跳转到搜索聊天室页面，并附带查询的聊天室信息
    return render(request, 'xitong/sousuochat.html', {"chatall": chatall});


#  处理聊天室详情   
def chatxiangqing(request, id):
    #  根据页面传入id获取聊天室信息
    chat = models.Chat.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到聊天室详情页面,并聊天室信息传递到页面中
    return render(request, 'xitong/chatxiangqing.html', {"chat": chat});


#  定义跳转user添加聊天室页面的方法  
def usertianjiachat(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加聊天室页面
    return render(request, 'xitong/usertianjiachat.html', {'userall': userall, 'teamall': teamall, });


#  处理添加聊天室方法   
def usertianjiachatact(request):
    #  从页面post数据中获取发信人
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取发信人id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取发言时间
    addtimestr = request.POST.get("addtime");
    addtime = "";
    if (addtimestr is not None):
        addtime = addtimestr;

    #  从页面post数据中获取发言内容
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

    #  将聊天室的属性赋值给聊天室，生成聊天室对象
    chat = models.Chat(user=user, userid=userid, addtime=addtime, content=content, team=team, teamid=teamid, );

    #  调用save方法保存聊天室信息
    chat.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加聊天室成功,并跳转到聊天室管理页面
    return HttpResponse(u"<p>添加聊天室成功</p><a href='/chat/userchatguanli'>返回页面</a>");


#  跳转user聊天室管理页面
def userchatguanli(request):
    #  查询出userid等于当前用户id的所有聊天室信息
    chatall = models.Chat.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回聊天室管理页面，并携带chatall的数据信息
    return render(request, 'xitong/userchatguanli.html', {'chatall': chatall});


#  定义跳转user修改聊天室页面      
def userxiugaichat(request, id):
    #  根据页面传入的聊天室id信息，查询出对应的聊天室信息
    chat = models.Chat.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  跳转到修改聊天室页面，并携带查询出的聊天室信息
    return render(request, 'xitong/userxiugaichat.html', {'chat': chat, 'userall': userall, 'teamall': teamall, });


#  定义处理修改聊天室方法   
def userxiugaichatact(request):
    #  使用request获取post中的聊天室id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的聊天室id获取对应的聊天室信息
    chat = models.Chat.objects.get(id=id);

    #  从页面post数据中获取发信人并赋值给chat的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        chat.user = userstr;

    #  从页面post数据中获取发信人id并赋值给chat的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        chat.userid = useridstr;

    #  从页面post数据中获取发言时间并赋值给chat的addtime字段
    addtimestr = request.POST.get("addtime");
    if (addtimestr is not None):
        chat.addtime = addtimestr;

    #  从页面post数据中获取发言内容并赋值给chat的content字段
    contentstr = request.POST.get("content");
    if (contentstr is not None):
        chat.content = contentstr;

    #  从页面post数据中获取团队并赋值给chat的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        chat.team = teamstr;

    #  从页面post数据中获取团队id并赋值给chat的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        chat.teamid = teamidstr;

    #  调用save方法保存聊天室信息
    chat.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改聊天室成功,并跳转到聊天室管理页面
    return HttpResponse(u"<p>修改聊天室成功</p><a href='/chat/userchatguanli'>返回页面</a>");


#  定义user删除聊天室信息
def usershanchuchatact(request, id):
    #  根据页面传入的聊天室id信息，删除出对应的聊天室信息
    models.Chat.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除聊天室成功，并跳转到聊天室管理页面
    return HttpResponse(u"<p>删除聊天室成功</p><a href='/chat/userchatguanli'>返回页面</a>");
