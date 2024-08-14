from django.urls import path
from django.views.generic import TemplateView
from samples.views import upload_file


#별칭
app_name = 'samples'


urlpatterns = [
    path('', TemplateView.as_view(template_name=app_name + '/index.html'), name='index'),
    path('fileupload', upload_file, name='upload_file'),
]

#path('upload/', views.upload_file, name='upload_file'),
#path('upload/success/', views.upload_success, name='file_upload_success')