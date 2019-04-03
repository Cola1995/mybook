"""mybook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views,urls

urlpatterns = [
    #出版社路径
    # url(r'^admin/', admin.site.urls),
    url(r'^plisher_list/', views.plisher_list),
    url(r'^add_plisher/', views.add_plisher),
    url(r'^delete_plisher/', views.delete_plisher),
    # url(r'^delete_plisher/([0-9]+)', views.delete_plisher2),
    url(r'^edit_plisher/', views.edit_plisher),

    #book路径
    url(r'^book_list/', views.book_list),
    url(r'^add_book/', views.add_book),
    url(r'^edit_book/', views.edit_book),

    #作者路径
    url(r'^author_list/', views.author_list),
    url(r'^add_author/', views.add_author),
    url(r'^del_author/', views.del_author),
    url(r'^edit_author/', views.edit_author),


    url(r'^test/', views.test),
    url(r'^upload/', views.upload),
    url(r'^json_data/', views.json_test),
    # url(r'^title/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.title),   #关键字参数传值
    url(r'^title/([0-9]+)/([0-9]+)/$', views.title),   #位置参数传值
    # url(r'^title/(?P<year>year[0-9]{2,4})/(?P<mouth>[0-9]{1})/$', views.title),
    # url(r'^title/(?P<year>[0-9]{2,4})/(?P<month>[a-zA-Z]{2})/$', views.title),
    # url(r'^title/(?P<year>[0-9]+)/(?P<month>[a-zA-Z]+)/$', views.title),

    url(r'^app01',include(urls)), #路由分发给app_01  /app_01/home/
    url(r'^trans/', views.trans),



]
