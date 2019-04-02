from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    #出版社路径
    # url(r'^admin/', admin.site.urls),
    url(r'^/home/', views.home,name="home"),

]