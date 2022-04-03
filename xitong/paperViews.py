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
import docx
from docx import Document
import PyPDF2
import sys
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import MySQLdb
import heapq
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import jieba
import jieba.posseg as pseg
import jieba.analyse


db = MySQLdb.connect("localhost","root","root","documentcollaboration",charset = 'utf8')
cursor = db.cursor()




def paperguilei():
    cursor.execute("select id,content from xitong_paper");
    xunlianwenbenall = cursor.fetchall();

    corpus = []  # 第四类文本的切词结果

    for xunlianwenben in xunlianwenbenall:
        # neirong = jieba.cut(xunlianwenben[1]);
        neirong = xunlianwenben[1];
        corpus.append(neirong)

    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(
        vectorizer.fit_transform(corpus))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        print
        u"-------这里输出第", i, u"类文本的词语tf-idf权重------";

        # 获取数据的编号 获取数据库对应的id
        id = xunlianwenbenall[i][0];
        # 获取对应的tfidf词 权重最高的四个词
        weighttemp = weight[i].tolist();
        re2 = map(weighttemp.index, heapq.nlargest(5, weighttemp))
        qc = [];
        print
        len(re2)
        for j in list(re2):
            # print word[j]
            qc.append(word[j])

        # if(qc[3] == qc[2] and qc[2] == qc[1]):
        #     wxneirongfenci = xunlianwenbenall[i][1].split(" ");
        #     qc[0] = wxneirongfenci[0];
        #     qc[1] = wxneirongfenci[1];
        #     qc[2] = wxneirongfenci[2];
        #     qc[3] = wxneirongfenci[3];

        sql = "update xitong_paper set tfidfci1 = '" + str(qc[0]) + "',tfidfci2 = '" + str(
            qc[1]) + "',tfidfci3 = '" + str(qc[2]) + "',tfidfci4 = '" + str(qc[3]) + "' where id = " + str(id);

        # print(sql);
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # i += 1
        except:
            # Rollback in case there is any error
            db.rollback()

        # for j in range(len(word)):
        #     print word[j], weight[i][j]

        # 执行数据库修改命令


    # from sklearn import datasets

    quenum = models.Paper.objects.all().count();


    if(quenum >= 100):
        fenleishuliang = int(quenum / 13);


    if(quenum <=100 and quenum >= 20):
        fenleishuliang = 9;

    if (quenum <= 20 and quenum >= 10):
        fenleishuliang = 5;

    if (quenum <= 10 and quenum >= 4):
        fenleishuliang = 4;

    if (quenum <= 3 and quenum >= 0):
        fenleishuliang = 3;

    X = weight

    estimator = KMeans(n_clusters=fenleishuliang)  # 构造聚类器
    estimator.fit(X)  # 聚类
    label_pred = estimator.labels_  # 获取聚类标签

    fenlei = [];
    result = [];
    resultid = [];

    for i in range(fenleishuliang):
        fenlei.append([])
        result.append([])
        resultid.append([])

    # 获取中心点
    # print u"中心点";
    # print estimator.cluster_centers_[0];
    for i in range(len(word)):
        for j in range(fenleishuliang):
            if (estimator.cluster_centers_[j][i] > 0.4):
                # print word[i],estimator.cluster_centers_[0][i]
                fenlei[j].append(word[i]);

    # 每个样本所属的簇
    print
    u"打印簇";

    x0 = X[label_pred == 0]
    x1 = X[label_pred == 1]
    x2 = X[label_pred == 2]
    x3 = X[label_pred == 3]

    # print u"第一类:"
    # print x0;
    # print u"第二类:"
    # print x1;
    # print u"第三类:"
    # print x2;
    # print u"第四类:"
    # print x3;


    for i in range(len(estimator.labels_)):
        for j in range(fenleishuliang):
            if (estimator.labels_[i - 1] == j):
                result[j].append(corpus[i - 1]);
                resultid[j].append(xunlianwenbenall[i - 1][0]);

    for i in range(fenleishuliang):

        guanjianci = "";
        for j in range(len(fenlei[i])):
            guanjianci += " " + fenlei[i][j];

        if (len(fenlei[i]) < 4):

            if(len(resultid[i]) > 0):
                cursor.execute(
                    "select biaoqian1,biaoqian2,biaoqian3,biaoqian4 from xitong_paper where id = " + str(
                        resultid[i][0]));
                xunlianwenben = cursor.fetchall()[0];
                guanjianci = xunlianwenben[0] + " " + xunlianwenben[1] + " " + xunlianwenben[2] + " " + xunlianwenben[3];

        guanjiancis = guanjianci.split(" ");

        baohanshuju = "";
        for j in range(len(result[i])):
            baohanshuju += " " + result[i][j];

        baohanshujuid = "";
        for j in range(len(resultid[i])):
            baohanshujuid += " " + str(resultid[i][j]);

            sql = "update xitong_paper set kmeansci1 = '" + str(guanjiancis[0]) + "',kmeansci2 = '" + str(
                guanjiancis[1]) + "',kmeansci3 = '" + str(guanjiancis[2]) + "',kmeansci4 = '" + str(
                guanjiancis[3]) + "' where id = " + str(resultid[i][j]);

            # print(sql);
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
                # i += 1
            except:
                # Rollback in case there is any error
                db.rollback()

        # print u"第", i, u"类关键词：", guanjianci, u"包含数据：", baohanshujuid;


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


#    定义添加论文的方法，响应页面请求
def tianjiapaper(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回添加论文页面，并将该页面数据传递到视图中
    return render(request, 'xitong/tianjiapaper.html', {'userall': userall, });


#  处理添加论文方法
def tianjiapaperact(request):
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

    #  从页面post数据中获取标签1
    biaoqian1str = request.POST.get("biaoqian1");
    biaoqian1 = "";
    if (biaoqian1str is not None):
        biaoqian1 = biaoqian1str;

    #  从页面post数据中获取标签2
    biaoqian2str = request.POST.get("biaoqian2");
    biaoqian2 = "";
    if (biaoqian2str is not None):
        biaoqian2 = biaoqian2str;

    #  从页面post数据中获取标签3
    biaoqian3str = request.POST.get("biaoqian3");
    biaoqian3 = "";
    if (biaoqian3str is not None):
        biaoqian3 = biaoqian3str;

    #  从页面post数据中获取标签4
    biaoqian4str = request.POST.get("biaoqian4");
    biaoqian4 = "";
    if (biaoqian4str is not None):
        biaoqian4 = biaoqian4str;

    #  从页面post数据中获取tfidf词1
    tfidfci1str = request.POST.get("tfidfci1");
    tfidfci1 = "";
    if (tfidfci1str is not None):
        tfidfci1 = tfidfci1str;

    #  从页面post数据中获取tfidf词2
    tfidfci2str = request.POST.get("tfidfci2");
    tfidfci2 = "";
    if (tfidfci2str is not None):
        tfidfci2 = tfidfci2str;

    #  从页面post数据中获取tfidf词3
    tfidfci3str = request.POST.get("tfidfci3");
    tfidfci3 = "";
    if (tfidfci3str is not None):
        tfidfci3 = tfidfci3str;

    #  从页面post数据中获取tfidf词4
    tfidfci4str = request.POST.get("tfidfci4");
    tfidfci4 = "";
    if (tfidfci4str is not None):
        tfidfci4 = tfidfci4str;

    #  从页面post数据中获取kmeans词1
    kmeansci1str = request.POST.get("kmeansci1");
    kmeansci1 = "";
    if (kmeansci1str is not None):
        kmeansci1 = kmeansci1str;

    #  从页面post数据中获取kmeans词2
    kmeansci2str = request.POST.get("kmeansci2");
    kmeansci2 = "";
    if (kmeansci2str is not None):
        kmeansci2 = kmeansci2str;

    #  从页面post数据中获取kmeans词3
    kmeansci3str = request.POST.get("kmeansci3");
    kmeansci3 = "";
    if (kmeansci3str is not None):
        kmeansci3 = kmeansci3str;

    #  从页面post数据中获取kmeans词4
    kmeansci4str = request.POST.get("kmeansci4");
    kmeansci4 = "";
    if (kmeansci4str is not None):
        kmeansci4 = kmeansci4str;

    #  从页面post数据中获取权限
    jurisdictionstr = request.POST.get("jurisdiction");
    jurisdiction = "";
    if (jurisdictionstr is not None):
        jurisdiction = jurisdictionstr;

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

    #  调用uploadFile方法上传页面中文件
    file = uploadFile(request, "filefile");

    #  将论文的属性赋值给论文，生成论文对象
    paper = models.Paper(title=title, addtime=addtime, content=content, biaoqian1=biaoqian1, biaoqian2=biaoqian2,
                         biaoqian3=biaoqian3, biaoqian4=biaoqian4, tfidfci1=tfidfci1, tfidfci2=tfidfci2,
                         tfidfci3=tfidfci3, tfidfci4=tfidfci4, kmeansci1=kmeansci1, kmeansci2=kmeansci2,
                         kmeansci3=kmeansci3, kmeansci4=kmeansci4, jurisdiction=jurisdiction, user=user, userid=userid,
                         state=state, file=file, );

    #  调用save方法保存论文信息
    paper.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加论文成功,并跳转到论文管理页面
    return HttpResponse(u"<p>添加论文成功</p><a href='/paper/paperguanli'>返回页面</a>");


#  定义表名管理方法，响应页面paperguanli请求
def paperguanli(request):
    #  通过all方法查询所有的论文信息
    paperall = models.Paper.objects.all()

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到论文管理页面，并附带所有论文信息
    return render(request, 'xitong/paperguanli.html', {'paperall': paperall});



#  定义修改论文方法，通过id查询对应的论文信息，返回页面展示
def papertuijian(request):

   # 当前用户上传的论文中随机获取一篇
    paperuserall = models.Paper.objects.filter(userid=request.session["id"]).order_by('?')[:1];

    paperall = [];

    if (paperuserall.count() > 0):
        paperitem = paperuserall[0];
        paperall = models.Paper.objects.filter(kmeansci1=paperitem.kmeansci1,kmeansci2=paperitem.kmeansci2,kmeansci3=paperitem.kmeansci3,kmeansci4=paperitem.kmeansci4,).all();
    else:
        paperall = models.Paper.objects.all();

    #  跳转到修改论文页面，并附带当前论文信息
    return render(request, 'xitong/papertuijian.html', {'paperall': paperall });

#  定义表名查看方法，响应页面paperchakan请求
def paperchakan(request):
    #  通过all方法查询所有的论文信息

    paperall = [];

    # 获取自己可见论文
    paperall1 = models.Paper.objects.filter(userid=request.session["id"],jurisdiction="自己可见").all();

    # 获取团队可见论文

    userids = [-1];
    # 获取自己创建的团队成员
    teams = models.Team.objects.filter(userid=request.session['id']).all();

    for team in teams:
        teammebers = models.Teammembers.objects.filter(teamid=team.id).all();

        for teammeber in teammebers:
            userids.append(teammeber.userid);


    # 获取自己参与的团队成员
    myteams = models.Teammembers.objects.filter(userid=request.session['id']).all();

    for myteam in myteams:
        teammebers = models.Teammembers.objects.filter(teamid=myteam.teamid).all();

        for teammeber in teammebers:
            userids.append(teammeber.userid);


    paperall2 = models.Paper.objects.filter(userid__in=userids, jurisdiction="团队可见").all();

    # 获取公众可见论文
    paperall3 = models.Paper.objects.filter(jurisdiction="公众可见").all();

    # 获取负责人可见论文

    # 获取自己创建团队的团队成员id
    userids = [-1];
    # 获取自己创建的团队成员
    teams = models.Team.objects.filter(userid=request.session['id']).all();

    for team in teams:
        teammebers = models.Teammembers.objects.filter(teamid=team.id).all();

        for teammeber in teammebers:
            userids.append(teammeber.userid);

    paperall4 = models.Paper.objects.filter(jurisdiction="负责人可见",userid__in=userids).all();

    paperall.extend(paperall1)
    paperall.extend(paperall2)
    paperall.extend(paperall3)
    paperall.extend(paperall4)
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到论文查看页面，并附带所有论文信息
    return render(request, 'xitong/paperchakan.html', {'paperall': paperall});


#  定义修改论文方法，通过id查询对应的论文信息，返回页面展示
def xiugaipaper(request, id):
    #  使用get方法，通过id查询对应的论文信息
    paper = models.Paper.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改论文页面，并附带当前论文信息
    return render(request, 'xitong/xiugaipaper.html', {'paper': paper, 'userall': userall, });


#  定义处理修改论文方法
def xiugaipaperact(request):
    #  使用request获取post中的论文id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的论文id获取对应的论文信息
    paper = models.Paper.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给paper的title字段
    titlestr = request.POST.get("title");
    if (titlestr is not None):
        paper.title = titlestr;

    #  从页面post数据中获取发布时间并赋值给paper的addtime字段
    addtimestr = request.POST.get("addtime");
    if (addtimestr is not None):
        paper.addtime = addtimestr;

    #  从页面post数据中获取内容并赋值给paper的content字段
    contentstr = request.POST.get("content");
    if (contentstr is not None):
        paper.content = contentstr;

    #  从页面post数据中获取标签1并赋值给paper的biaoqian1字段
    biaoqian1str = request.POST.get("biaoqian1");
    if (biaoqian1str is not None):
        paper.biaoqian1 = biaoqian1str;

    #  从页面post数据中获取标签2并赋值给paper的biaoqian2字段
    biaoqian2str = request.POST.get("biaoqian2");
    if (biaoqian2str is not None):
        paper.biaoqian2 = biaoqian2str;

    #  从页面post数据中获取标签3并赋值给paper的biaoqian3字段
    biaoqian3str = request.POST.get("biaoqian3");
    if (biaoqian3str is not None):
        paper.biaoqian3 = biaoqian3str;

    #  从页面post数据中获取标签4并赋值给paper的biaoqian4字段
    biaoqian4str = request.POST.get("biaoqian4");
    if (biaoqian4str is not None):
        paper.biaoqian4 = biaoqian4str;

    #  从页面post数据中获取tfidf词1并赋值给paper的tfidfci1字段
    tfidfci1str = request.POST.get("tfidfci1");
    if (tfidfci1str is not None):
        paper.tfidfci1 = tfidfci1str;

    #  从页面post数据中获取tfidf词2并赋值给paper的tfidfci2字段
    tfidfci2str = request.POST.get("tfidfci2");
    if (tfidfci2str is not None):
        paper.tfidfci2 = tfidfci2str;

    #  从页面post数据中获取tfidf词3并赋值给paper的tfidfci3字段
    tfidfci3str = request.POST.get("tfidfci3");
    if (tfidfci3str is not None):
        paper.tfidfci3 = tfidfci3str;

    #  从页面post数据中获取tfidf词4并赋值给paper的tfidfci4字段
    tfidfci4str = request.POST.get("tfidfci4");
    if (tfidfci4str is not None):
        paper.tfidfci4 = tfidfci4str;

    #  从页面post数据中获取kmeans词1并赋值给paper的kmeansci1字段
    kmeansci1str = request.POST.get("kmeansci1");
    if (kmeansci1str is not None):
        paper.kmeansci1 = kmeansci1str;

    #  从页面post数据中获取kmeans词2并赋值给paper的kmeansci2字段
    kmeansci2str = request.POST.get("kmeansci2");
    if (kmeansci2str is not None):
        paper.kmeansci2 = kmeansci2str;

    #  从页面post数据中获取kmeans词3并赋值给paper的kmeansci3字段
    kmeansci3str = request.POST.get("kmeansci3");
    if (kmeansci3str is not None):
        paper.kmeansci3 = kmeansci3str;

    #  从页面post数据中获取kmeans词4并赋值给paper的kmeansci4字段
    kmeansci4str = request.POST.get("kmeansci4");
    if (kmeansci4str is not None):
        paper.kmeansci4 = kmeansci4str;

    #  从页面post数据中获取权限并赋值给paper的jurisdiction字段
    jurisdictionstr = request.POST.get("jurisdiction");
    if (jurisdictionstr is not None):
        paper.jurisdiction = jurisdictionstr;

    #  从页面post数据中获取用户并赋值给paper的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        paper.user = userstr;

    #  从页面post数据中获取用户id并赋值给paper的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        paper.userid = useridstr;

    #  从页面post数据中获取状态并赋值给paper的state字段
    statestr = request.POST.get("state");
    if (statestr is not None):
        paper.state = statestr;

    #  调用uploadFile方法上传页面中文件
    filefile = uploadFile(request, "filefile");

    #  如果filefile不等于false
    if (filefile != "false"):
        #  将filefile赋值给论文的文件字段
        paper.file = filefile;

    #  调用save方法保存论文信息
    paper.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改论文成功,并跳转到论文管理页面
    return HttpResponse(u"<p>修改论文成功</p><a href='/paper/paperguanli'>返回页面</a>");


#  定义删除论文方法
def shanchupaperact(request, id):
    #  调用django的delete方法，根据id删除论文信息
    models.Paper.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,删除论文成功,并跳转到论文管理页面
    return HttpResponse(u"<p>删除论文成功</p><a href='/paper/paperguanli'>返回页面</a>");


#  定义搜索论文方法，响应页面搜索请求
def sousuopaper(request):
    #  获取页面post参数中的search信息
    search = request.POST.get("search");

    #  如果search为None
    if (search is None):
        #  设置search等于空字符串
        search = "";

    #  使用django的filter方法过滤查询包含search的论文信息
    paperall = models.Paper.objects.filter(title__icontains=search);

    #  跳转到搜索论文页面，并附带查询的论文信息
    return render(request, 'xitong/sousuopaper.html', {"paperall": paperall});


#  处理论文详情
def paperxiangqing(request, id):
    #  根据页面传入id获取论文信息
    paper = models.Paper.objects.get(id=id);

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  跳转到论文详情页面,并论文信息传递到页面中
    return render(request, 'xitong/paperxiangqing.html', {"paper": paper});


#  定义跳转user添加论文页面的方法
def usertianjiapaper(request):
    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回user添加论文页面
    return render(request, 'xitong/usertianjiapaper.html', {'userall': userall, });


#  处理添加论文方法
def usertianjiapaperact(request):
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

    #  从页面post数据中获取权限
    jurisdictionstr = request.POST.get("jurisdiction");
    jurisdiction = "";
    if (jurisdictionstr is not None):
        jurisdiction = jurisdictionstr;

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

    #  调用uploadFile方法上传页面中文件
    file = uploadFile(request, "filefile");


    if(file.endswith(".docx")):
        docStr = Document("C:\Users\Administrator\Desktop\documentcollaboration/static/upload/" + file)  # 打开文档

        neirong = "";
        for paragraph in docStr.paragraphs:
            parStr = paragraph.text
            neirong = neirong + parStr + "\n";
    elif(file.endswith(".txt")):
        with open("C:\Users\Administrator\Desktop\documentcollaboration/static/upload/" + file, "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            neirong = data;

    elif (file.endswith(".pdf")):
        pdffile = open(r"C:\Users\Administrator\Desktop\documentcollaboration/static/upload/" + file, 'rb')  # 读取pdf文件

        pdfreader = PyPDF2.PdfFileReader(pdffile)  # 读入到

        print(pdfreader.numPages)  # 读取pdf页数======19

        neirong = "";
        for i in range(pdfreader.numPages):
            pageitem = pdfreader.getPage(i);
            neirong = neirong + str(pageitem.extractText()) + "\n";

    else:
        return HttpResponse(u"<p>文档格式错误，仅支持txt、pdf、dpcx</p><a href='/paper/userpaperguanli'>返回页面</a>");


    biaoqians = jieba.analyse.extract_tags(neirong, topK=5, withWeight=True, allowPOS=())
    biaoqian1 = "";
    biaoqian2 = "";
    biaoqian3 = "";
    biaoqian4 = "";
    if (len(biaoqians) > 0):
        biaoqian1 = biaoqians[0][0];
    if (len(biaoqians) > 1):
        biaoqian2 = biaoqians[1][0];
    if (len(biaoqians) > 2):
        biaoqian3 = biaoqians[2][0];
    if (len(biaoqians) > 3):
        biaoqian4 = biaoqians[3][0];

    #  将论文的属性赋值给论文，生成论文对象
    paper = models.Paper(title=title, addtime=addtime, content=neirong, jurisdiction=jurisdiction, user=user, userid=userid,
                         state=state, file=file,biaoqian1=biaoqian1,biaoqian2=biaoqian2,biaoqian3=biaoqian3,biaoqian4=biaoqian4, );

    #  如果backurl不等于none
    if ( len(neirong) < 50):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>文本内容长度低于50字符，上传失败</p><a href='/paper/userpaperguanli'>返回页面</a>");

    #  调用save方法保存论文信息
    paper.save();
    paperguilei()
    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");
    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,添加论文成功,并跳转到论文管理页面
    return HttpResponse(u"<p>添加论文成功</p><a href='/paper/userpaperguanli'>返回页面</a>");


#  跳转user论文管理页面
def userpaperguanli(request):
    #  查询出userid等于当前用户id的所有论文信息
    paperall = models.Paper.objects.filter(userid=request.session["id"])

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回论文管理页面，并携带paperall的数据信息
    return render(request, 'xitong/userpaperguanli.html', {'paperall': paperall});


#  定义跳转user修改论文页面      
def userxiugaipaper(request, id):
    #  根据页面传入的论文id信息，查询出对应的论文信息
    paper = models.Paper.objects.get(id=id);

    #  获取页面数据user,使用DJANGO all方法查询所有数据
    userall = models.User.objects.all();

    #  跳转到修改论文页面，并携带查询出的论文信息
    return render(request, 'xitong/userxiugaipaper.html', {'paper': paper, 'userall': userall, });


#  定义处理修改论文方法   
def userxiugaipaperact(request):
    #  使用request获取post中的论文id参数
    id = request.POST.get("id");

    #  使用model的get方法根据页面传入的论文id获取对应的论文信息
    paper = models.Paper.objects.get(id=id);

    #  从页面post数据中获取标题并赋值给paper的title字段
    titlestr = request.POST.get("title");
    if (titlestr is not None):
        paper.title = titlestr;

    #  从页面post数据中获取发布时间并赋值给paper的addtime字段
    addtimestr = request.POST.get("addtime");
    if (addtimestr is not None):
        paper.addtime = addtimestr;

    #  从页面post数据中获取内容并赋值给paper的content字段
    contentstr = request.POST.get("content");
    if (contentstr is not None):
        paper.content = contentstr;

    #  从页面post数据中获取标签1并赋值给paper的biaoqian1字段
    biaoqian1str = request.POST.get("biaoqian1");
    if (biaoqian1str is not None):
        paper.biaoqian1 = biaoqian1str;

    #  从页面post数据中获取标签2并赋值给paper的biaoqian2字段
    biaoqian2str = request.POST.get("biaoqian2");
    if (biaoqian2str is not None):
        paper.biaoqian2 = biaoqian2str;

    #  从页面post数据中获取标签3并赋值给paper的biaoqian3字段
    biaoqian3str = request.POST.get("biaoqian3");
    if (biaoqian3str is not None):
        paper.biaoqian3 = biaoqian3str;

    #  从页面post数据中获取标签4并赋值给paper的biaoqian4字段
    biaoqian4str = request.POST.get("biaoqian4");
    if (biaoqian4str is not None):
        paper.biaoqian4 = biaoqian4str;

    #  从页面post数据中获取tfidf词1并赋值给paper的tfidfci1字段
    tfidfci1str = request.POST.get("tfidfci1");
    if (tfidfci1str is not None):
        paper.tfidfci1 = tfidfci1str;

    #  从页面post数据中获取tfidf词2并赋值给paper的tfidfci2字段
    tfidfci2str = request.POST.get("tfidfci2");
    if (tfidfci2str is not None):
        paper.tfidfci2 = tfidfci2str;

    #  从页面post数据中获取tfidf词3并赋值给paper的tfidfci3字段
    tfidfci3str = request.POST.get("tfidfci3");
    if (tfidfci3str is not None):
        paper.tfidfci3 = tfidfci3str;

    #  从页面post数据中获取tfidf词4并赋值给paper的tfidfci4字段
    tfidfci4str = request.POST.get("tfidfci4");
    if (tfidfci4str is not None):
        paper.tfidfci4 = tfidfci4str;

    #  从页面post数据中获取kmeans词1并赋值给paper的kmeansci1字段
    kmeansci1str = request.POST.get("kmeansci1");
    if (kmeansci1str is not None):
        paper.kmeansci1 = kmeansci1str;

    #  从页面post数据中获取kmeans词2并赋值给paper的kmeansci2字段
    kmeansci2str = request.POST.get("kmeansci2");
    if (kmeansci2str is not None):
        paper.kmeansci2 = kmeansci2str;

    #  从页面post数据中获取kmeans词3并赋值给paper的kmeansci3字段
    kmeansci3str = request.POST.get("kmeansci3");
    if (kmeansci3str is not None):
        paper.kmeansci3 = kmeansci3str;

    #  从页面post数据中获取kmeans词4并赋值给paper的kmeansci4字段
    kmeansci4str = request.POST.get("kmeansci4");
    if (kmeansci4str is not None):
        paper.kmeansci4 = kmeansci4str;

    #  从页面post数据中获取权限并赋值给paper的jurisdiction字段
    jurisdictionstr = request.POST.get("jurisdiction");
    if (jurisdictionstr is not None):
        paper.jurisdiction = jurisdictionstr;

    #  从页面post数据中获取用户并赋值给paper的user字段
    userstr = request.POST.get("user");
    if (userstr is not None):
        paper.user = userstr;

    #  从页面post数据中获取用户id并赋值给paper的userid字段
    useridstr = request.POST.get("userid");
    if (useridstr is not None):
        paper.userid = useridstr;

    #  从页面post数据中获取状态并赋值给paper的state字段
    statestr = request.POST.get("state");
    if (statestr is not None):
        paper.state = statestr;

    #  调用uploadFile方法上传页面中文件
    filefile = uploadFile(request, "filefile");

    #  如果filefile不等于false
    if (filefile != "false"):
        #  将filefile赋值给论文的文件字段
        paper.file = filefile;

    #  调用save方法保存论文信息
    paper.save();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  返回页面提示信息,修改论文成功,并跳转到论文管理页面
    return HttpResponse(u"<p>修改论文成功</p><a href='/paper/userpaperguanli'>返回页面</a>");


#  定义user删除论文信息
def usershanchupaperact(request, id):
    #  根据页面传入的论文id信息，删除出对应的论文信息
    models.Paper.objects.filter(id=id).delete();

    #  获取页面数据中的backurl参数
    backurl = request.POST.get("backurl");

    #  如果backurl不等于none
    if (backurl is not None):
        #  返回操作成功，并跳转到backurl链接处
        return HttpResponse(u"<p>操作成功</p><a href='" + backurl + u"'>返回页面</a>");

    #  在页面给出提示信息，删除论文成功，并跳转到论文管理页面
    return HttpResponse(u"<p>删除论文成功</p><a href='/paper/userpaperguanli'>返回页面</a>");
