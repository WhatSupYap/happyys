from django.urls import path
from django.views.generic import TemplateView
from . import views


"""
앱 별칭: 별칭을 지정해주면 템플릿에서 url별칭 앞에 app_name을 붙여서 사용해야한다.
예: {% url 'index' %} -> {% url 'app_name:index' %}
"""
app_name = 'blog'

# URL 별칭이 있어서 URL에 신경을 쓰지 않아도 된다.
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='post_detail'),
    path("l/", views.post_list, name='post_list'),
    path('pw/', views.post_write, name='post_write'),
    path('pwr/<int:post_id>/', views.post_write_re, name='post_wirte_re'),
    path('rw/<int:post_id>/', views.reply_write, name='reply_write'),
    path('pd/<int:post_id>/', views.post_remove, name='post_remove'),
    path('rwr/<int:reply_id>/', views.reply_write_re, name='reply_write_re'),
]
