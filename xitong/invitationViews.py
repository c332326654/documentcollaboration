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


#    定义添加邀请的方法，响应页面请求
def tianjiainvitation(request):
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

    #  返回添加邀请页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiainvitation.html', {'teamall': teamall, 'userall': userall, });


#  处理添加邀请方法   
def tianjiainvitationact(request):
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

    #  从页面post数据中获取用户
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取用户id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取状态
    statestr = request.POST.get("state");
    state = "";
    if (statestr is not None):
        state = statestr;

    useritem = models.User.objects.filter(id=userid).all();
    if(useritem.count() == 0):
        return HttpResponse(u"<p>用户ID不存在</p><a href='/team/userteamguanli/'>返回页面</a>");
    teammembers = models.Teammembers.objects.filter(userid=userid,teamid=teamid);
    if(teammembers.count() >0):
        return HttpResponse(u"<p>该用户已在团队中，邀请失败</p><a href='/team/userteamguanli/'>返回页面</a>");
    teamitem = models.Team.objects.get(id=teamid);
    #  将邀请的属性赋值给邀请，生成邀请对象
    invitation = models.Invitation(team=teamitem.name, teamid=teamid, user=useritem[0].name, userid=userid, state=state, );
    #  调用save方法保存邀请信息
    invitation.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加邀请成功,并跳转到邀请管理页面
    return HttpResponse(u"<p>添加邀请成功</p><a href='/team/userteamguanli/'>返回页面</a>");


#  定义表名管理方法，响应页面invitationguanli请求   
def invitationguanli(request):
    #  通过all方法查询所有的邀请信息
    invitationall = models.Invitation.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到邀请管理页面，并附带所有邀请信息
    return render(request, 'xitong/invitationguanli.html', {'invitationall': invitationall});


#  定义表名查看方法，响应页面invitationchakan请求   
def invitationchakan(request):
    #  通过all方法查询所有的邀请信息
    invitationall = models.Invitation.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到邀请查看页面，并附带所有邀请信息
    return render(request, 'xitong/invitationchakan.html', {'invitationall': invitationall});


#  定义修改邀请方法，通过id查询对应的邀请信息，返回页面展示  
def xiugaiinvitation(request, id):
    #  使用get方法，通过id查询对应的邀请信息
    invitation = models.Invitation.objects.get(id=id);

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改邀请页面，并附带当前邀请信息
    return render(request, 'xitong/xiugaiinvitation.html',
                  {'invitation': invitation, 'teamall': teamall, 'userall': userall, });


#  定义处理修改邀请方法   
def xiugaiinvitationact(request):
    #  使用request获取post中的邀请id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的邀请id获取对应的邀请信息
    invitation = models.Invitation.objects.get(id=id);

    #  从页面post数据中获取团队并赋值给invitation的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        invitation.team = teamstr;

    #  从页面post数据中获取团队id并赋值给invitation的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        invitation.teamid = teamidstr;

    #  从页面post数据中获取用户并赋值给invitation的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        invitation.user = userstr;

    #  从页面post数据中获取用户id并赋值给invitation的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        invitation.userid = useridstr;

    #  从页面post数据中获取状态并赋值给invitation的state字段
    statestr = request.POST.get("state");
    if (statestr is not None):
        invitation.state = statestr;

    #  调用save方法保存邀请信息
    invitation.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改邀请成功,并跳转到邀请管理页面
    return HttpResponse(u"<p>修改邀请成功</p><a href='/invitation/invitationguanli'>返回页面</a>");


#  定义删除邀请方法   
def shanchuinvitationact(request, id):
    #  调用django的delete方法，根据id删除邀请信息
    models.Invitation.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除邀请成功,并跳转到邀请管理页面
    return HttpResponse(u"<p>删除邀请成功</p><a href='/invitation/invitationguanli'>返回页面</a>");


#  定义搜索邀请方法，响应页面搜索请求   
def sousuoinvitation(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的邀请信息
    invitationall = models.Invitation.objects.filter(team__icontains=search);

    #  跳转到搜索邀请页面，并附带查询的邀请信息
    return render(request, 'xitong/sousuoinvitation.html', {"invitationall": invitationall});


#  处理邀请详情   
def invitationxiangqing(request, id):
    #  根据页面传入id获取邀请信息
    invitation = models.Invitation.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到邀请详情页面,并邀请信息传递到页面中
    return render(request, 'xitong/invitationxiangqing.html', {"invitation": invitation});


#  定义跳转user添加邀请页面的方法  
def usertianjiainvitation(request):
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

    #  返回user添加邀请页面
    return render(request, 'xitong/usertianjiainvitation.html', {'teamall': teamall, 'userall': userall, });


#  处理添加邀请方法   
def usertianjiainvitationact(request):
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

    #  从页面post数据中获取用户
    userstr = request.POST.get("user");
    user = "";
    if (userstr is not None):
        user = userstr;

    #  从页面post数据中获取用户id
    useridstr = request.POST.get("userid");
    userid = "";
    if (useridstr is not None):
        userid = useridstr;

    #  从页面post数据中获取状态
    statestr = request.POST.get("state");
    state = "";
    if (statestr is not None):
        state = statestr;

    #  将邀请的属性赋值给邀请，生成邀请对象
    invitation = models.Invitation(team=team, teamid=teamid, user=user, userid=userid, state=state, );

    #  调用save方法保存邀请信息
    invitation.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加邀请成功,并跳转到邀请管理页面
    return HttpResponse(u"<p>添加邀请成功</p><a href='/invitation/userinvitationguanli'>返回页面</a>");


#  跳转user邀请管理页面
def userinvitationguanli(request):
    #  查询出userid等于当前用户id的所有邀请信息
    invitationall = models.Invitation.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回邀请管理页面，并携带invitationall的数据信息
    return render(request, 'xitong/userinvitationguanli.html', {'invitationall': invitationall});



#  定义跳转user修改邀请页面
def usertongyiinvitation(request, id):
    #  根据页面传入的邀请id信息，查询出对应的邀请信息
    invitation = models.Invitation.objects.get(id=id);

    invitation.state = '同意';

    invitation.save();

    invcass = models.Teammembers.objects.filter(teamid=invitation.teamid,userid=invitation.userid);

    if(invcass.count() == 0):
        models.Teammembers(team=invitation.team,teamid=invitation.teamid,user=invitation.user,userid=invitation.userid).save();

    #  跳转到修改邀请页面，并携带查询出的邀请信息
    return HttpResponse(u"<p>操作成功</p><a href='/invitation/userinvitationguanli/'>返回页面</a>");

#  定义跳转user修改邀请页面
def userjujueinvitation(request, id):
    #  根据页面传入的邀请id信息，查询出对应的邀请信息
    invitation = models.Invitation.objects.get(id=id);

    invitation.state = '拒绝';

    invitation.save();

    #  跳转到修改邀请页面，并携带查询出的邀请信息
    return HttpResponse(u"<p>操作成功</p><a href='/invitation/userinvitationguanli/'>返回页面</a>");

#  定义跳转user修改邀请页面      
def userxiugaiinvitation(request, id):
    #  根据页面传入的邀请id信息，查询出对应的邀请信息
    invitation = models.Invitation.objects.get(id=id);

    #  获取页面数据team,使用DJANGO all方法查询所有数据
    teamall = models.Team.objects.all();

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改邀请页面，并携带查询出的邀请信息
    return render(request, 'xitong/userxiugaiinvitation.html',
                  {'invitation': invitation, 'teamall': teamall, 'userall': userall, });


#  定义处理修改邀请方法   
def userxiugaiinvitationact(request):
    #  使用request获取post中的邀请id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的邀请id获取对应的邀请信息
    invitation = models.Invitation.objects.get(id=id);

    #  从页面post数据中获取团队并赋值给invitation的team字段
    teamstr = request.POST.get("team");
    if (teamstr is not None):
        invitation.team = teamstr;

    #  从页面post数据中获取团队id并赋值给invitation的teamid字段
    teamidstr = request.POST.get("teamid");
    if (teamidstr is not None):
        invitation.teamid = teamidstr;

    #  从页面post数据中获取用户并赋值给invitation的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        invitation.user = userstr;

    #  从页面post数据中获取用户id并赋值给invitation的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        invitation.userid = useridstr;

    #  从页面post数据中获取状态并赋值给invitation的state字段
    statestr = request.POST.get("state");
    if (statestr is not None):
        invitation.state = statestr;

    #  调用save方法保存邀请信息
    invitation.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改邀请成功,并跳转到邀请管理页面
    return HttpResponse(u"<p>修改邀请成功</p><a href='/invitation/userinvitationguanli'>返回页面</a>");


#  定义user删除邀请信息
def usershanchuinvitationact(request, id):
    #  根据页面传入的邀请id信息，删除出对应的邀请信息
    models.Invitation.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除邀请成功，并跳转到邀请管理页面
    return HttpResponse(u"<p>删除邀请成功</p><a href='/invitation/userinvitationguanli'>返回页面</a>");
