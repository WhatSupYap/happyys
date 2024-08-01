from django.urls import path
from django.views.generic import TemplateView


#별칭
app_name = 'isg'

urlpatterns = [
    path('', TemplateView.as_view(template_name='isg/index.html'), name='index'),
]
