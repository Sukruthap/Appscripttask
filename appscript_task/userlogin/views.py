# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile

# Create your views here.
def homepage(request):
    return render(request,'userlogin.html')

def login(request):
    if request.method == 'POST':
        # print "in post"
        user = auth.authenticate(username = request.POST['uname'],password = request.POST['pass'])
        print user
        # print user
        if user is not None and user.is_superuser:
            # print "in if"
            return HttpResponseRedirect('/adduser/')
            # return render(request,'adminuser.html')
        elif user is not None:
            # print "user is not none"
            # auth.login(request,user)
            # userdata = Profile.objects.all()
            # return render(request,'subuserview.html',{'userdata':userdata})
            return HttpResponseRedirect('/showuserdata/')
        else:
            # print "i am in else"
            return render(request,'userlogin.html',{'error':'Invalid credentials.'})
    else:
        return render(request,'userlogin.html')
# @login_required()
def adduser(request):
    if request.method == 'POST':
        print request.POST['username'],request.POST['state'],request.POST['pnumber'],request.POST['area']
        try:
            user = User.objects.get(username=request.POST['username'])
            userdata = Profile.objects.all()
            # print userdata, 'user already exist'
            return render(request,'adminuser.html',{'error':'User Already exist', 'userdata':userdata})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'],email=request.POST['email'])
            phonenumber = request.POST['pnumber']
            state = request.POST['state']
            area = request.POST['area']
            city = request.POST['city']
            extuser = Profile(user=user,phonenumber=phonenumber, area=area, state=state, city=city)
            extuser.save()
            auth.login(request,user)
            userdata = Profile.objects.all()
            # print userdata
            return render(request, 'adminuser.html', {'userdata': userdata})
    else:
        userdata = Profile.objects.all()
        # print userdata
        return render(request,'adminuser.html',{'userdata':userdata})


def deleteuser(request,pid):
    try:
        # print pid
        getuser = User.objects.get(id=pid)
        # print getuser
        getuser.profile.delete()
        getuser.delete()
        userdata = Profile.objects.all()
        # print userdata
        return render(request, 'adminuser.html', {'userdata': userdata})
    except User.DoesNotExist:
        print "I am in except"
        userdata = Profile.objects.all()
        # print userdata
        return render(request, 'adminuser.html', {'userdata': userdata})
def updateuser(request,pid):
    try:
        # print pid
        getuser = User.objects.get(id=pid)
    except User.DoesNotExist:
        return render(request,'adminuser.html',{'error':'Usernot found'})
    if request.method == 'POST':
        getuser.profile.phonenumber = request.POST['pnumber']
        getuser.profile.state = request.POST['state']
        getuser.profile.area = request.POST['area']
        getuser.profile.city = request.POST['city']
        getuser.email = request.POST['email']
        getuser.profile.save()
        getuser.save()
        return HttpResponseRedirect('/adduser/')
    else:
        return render(request,'updateuser.html',{'user':getuser})
def showuserdata(request):
    if request.method == 'GET':
        userdata = Profile.objects.all()
        # print userdata
        return render(request, 'subuserview.html', {'userdata': userdata})