from django.conf.urls import url
from userlogin import views

urlpatterns = [
    url(r'userlogin/',views.login, name='userlogin'),
    url(r'adduser/',views.adduser, name='adduser'),
    url(r'deleteuser/(?P<pid>\d+)/',views.deleteuser,name='deleteuser'),
    url(r'updateuser/(?P<pid>\d+)/',views.updateuser, name='updateuser'),
    url(r'showuserdata/',views.showuserdata, name='showuserdata'),
]