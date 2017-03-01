#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import comments
from django.contrib.contenttypes.models import ContentType
import models

# Create your views here.
def index(request):
    bbs_list=models.BBS.objects.all()
    bbs_categories=models.Category.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,
                                            'user':request.user,
                                            'bbs_category':bbs_categories,
                                            'cata_id':0})
def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj':bbs,'user':request.user})
def sub_comment(request):
    print request.POST
    
    bbs_id=request.POST.get('bbs_id')
    comment=request.POST.get('comment_content')

    comments.models.Comment.objects.create(
            content_type_id=7,
            object_pk=bbs_id,
            site_id=1,
            user=request.user, 
            comment=comment,
                                   )
    return HttpResponseRedirect('/detail/%s'%bbs_id)

def Login(request):
    return render_to_response('login.html')
def acc_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    print username,password
    if user is not None:
        auth.login(request, user)
        content='''
        Welcome %s !!!
        
        <a href='/logout/'>Logout</a>
        
        '''%user.username
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username' })
    
def logout_view(request):
    user=request.user 
    auth.logout(request)
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>Re-login</a>" % user)

def bbs_pub(request):
    return render_to_response('bbs_pub.html')
def bbs_sub(request):
    print request.POST.get('content')
    content=request.POST.get('content')
    #category_id=models.Category.objects.get(id=1)
    author=models.BBS_user.objects.get(user__username=request.user)
    models.BBS.objects.create(
         title ='test title',
        summary = 'HAHA',
        content = content,
        author =author,
        view_count= 1,
        ranking = 1,                   
        )
    return HttpResponse('yes')

def category(request,cata_id):
    bbs_list=models.BBS.objects.filter(category__id=cata_id)
    bbs_categories=models.Category.objects.all()
    return render_to_response('index.html',{'bbs_list':bbs_list,
                                            'user':request.user,
                                            'bbs_category':bbs_categories,
                                            'cata_id':int(cata_id)})
     



