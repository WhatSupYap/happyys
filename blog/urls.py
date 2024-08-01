from django.urls import path
from django.views.generic import TemplateView


#별칭
app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
]
