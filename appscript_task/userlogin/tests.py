# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import unittest
from django.test import Client
from .models import Profile

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/userlogin/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    def test_login(self):
        response = self.client.post('/userlogin/',{'uname': 'admin', 'pass': 'admintask'})
        self.assertEqual(response.status_code, 200)

    def test_adduser(self):
        userdata = Profile.objects.all()
        response = self.client.get('/adduser/',{'userdata':userdata})
        self.assertEqual(response.status_code, 200)
    def test_add_adduser(self):
        userdata = Profile.objects.all()
        response = self.client.post('/adduser/',{'userdata':userdata,'username':'abc','password':'abc','pnumber':'2563789212','state':'karnataka','area':'BTM','city':'Bangalore'})
        self.assertEqual(response.status_code, 200)
    def test_update(self):
        userdata = Profile.objects.all()
        userid = userdata[1].id
        response = self.client.get('/updateuser/%s',userid)
        self.assertEqual(response.status_code, 200)
    def test_update_value(self):
        userdata = Profile.objects.all()
        userid = userdata[1].id
        response = self.client.post('/updateuser/%s', userid,{'pnumber':'256783976','state':'Karnataka','area':'BTM','city':'Bangalore','email':'exp@exp.com'})
        self.assertEqual(response.status_code, 200)
    def test_update_value(self):
        userdata = Profile.objects.all()
        userid = userdata[1].id
        response = self.client.post('/updateuser/%s', userid,{'pnumber':'256783976','state':'Karnataka','area':'BTM','city':'Bangalore','email':'exp@exp.com'})
        self.assertEqual(response.status_code, 200)
    def test_delete_user(self):
        userdata = Profile.objects.all()
        i = len(userdata)-1
        userid = userdata[i].id
        response = self.client.get('/deleteuser/%s',userid)
        self.assertEqual(response.status_code, 200)
    def test_showuserdata(self):
        userdata = Profile.objects.all()
        response = self.client.get('/showuserdata/', {'userdata': userdata})
        self.assertEqual(response.status_code, 200)
