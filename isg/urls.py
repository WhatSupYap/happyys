from django.urls import path
from django.views.generic import TemplateView
from isg.views.monster_views import get_monster_list, create_monster
from isg.views.sogsag_views import set_sogsag, get_sogsag_list, del_sogsag


#별칭
app_name = 'isg'

urlpatterns = [
    path('', TemplateView.as_view(template_name='isg/index.html'), name='index'),
    # 몬스터를 만든다
    #path("m/create/",)
    path("m/list/", get_monster_list, name='get_monster_list'),
    path("m/create/", create_monster, name='create_monster'),
    # path('api/hello/', hello_rest_api, name='hello_rest_api'),
    path("depense", TemplateView.as_view(template_name='isg/depense.html'), name='depense'),
    path("s/create", set_sogsag, name='set_sogsag'),
    path("s/", TemplateView.as_view(template_name='isg/sogsagim.html'), name='sogsagim'),
    #path("s/l", TemplateView.as_view(template_name='isg/sogsagim_list.html'), name='sogsagim_list'),
    path("s/l", get_sogsag_list, name='get_sogsag_list'),
    path("s/d/<int:sogsag_id>", del_sogsag, name='sogsagim_delete'),
]
