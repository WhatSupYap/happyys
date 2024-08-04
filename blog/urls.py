from django.urls import path
from django.views.generic import TemplateView
#from blog.views import hello_rest_api


#별칭
app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
]
