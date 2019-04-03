# chat/urls.py
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginVerify/$', views.loginVerify, name='loginVerify'),
    url(r'register/$',views.register, name='register'),
    path('mail_detail/<int:id>/',views.mail_detail, name='mail_detail'),
    path('send_detail/<int:id>/',views.send_detail, name='send_detail'),
    path('undo_detail/<int:id>/',views.undo_detail, name='undo_detail'),
    url(r'^registerVerify/$', views.registerVerify, name='registerVerify'),
    url(r'search_friend/$',views.search_friend, name='search_friend'),
    url(r'^search_friendVerify/$', views.search_friendVerify, name='search_friendVerify'),
    url(r'home_page/$',views.home_page, name='home_page'),
    url(r'main_page/$',views.main_page, name='main_page'),
    url(r'write_email/$', views.write_email, name='write_email'),
    url(r'write_emailVerify/$', views.write_emailVerify, name='write_emailVerify'),
    url(r'mailbox/$', views.mailbox, name='mailbox'),
    url(r'sendbox/$', views.sendbox, name='sendbox'),
    url(r'undobox/$', views.undobox, name='undobox'),
    url(r'search_result/$', views.search_result, name='search_result'),
    url(r'change_password/$',views.change_password, name='change_password'),
    #url(r'home_page/^(?P<room_name>[^/]+)/$', views.home_page, name='room'),
]