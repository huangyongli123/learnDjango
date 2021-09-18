from django.conf.urls import url

from users import views

urlpatterns = [
    # 配置路由和视图: http://127.0.0.1:8000/users/index
    # 参数1： 匹配url的正则表达式
    # 参数2： 匹配成功后由Django框架调用的视图函数
    url(r'^index/$', views.index, name='index'),
    url(r'^(\d+)/(\d+)/$', views.hello),
    url(r'^new2/$', views.new2),
    url(r'^new3/$', views.new3),
    url(r'^new4/$', views.new4, name="new4"),
    url(r'^resp/$', views.resp),
    url(r'^resp1/$', views.resp1, name="resp1"),
    url(r'^redirect/$', views.my_redirect),
    url(r'^redirect1/$', views.my_redirect1)  # 若views.py里没有my_redirect1)这个方法，则报错
    # url(r'^hello/(\d+)\(\d+)$', views.index)

]
