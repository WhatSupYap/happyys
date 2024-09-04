from django.urls import path
from django.views.generic import TemplateView
from samples.views import *#upload_file, upload_file2, read_uploaded_file, add_sampledoc, get_sampledoc, goto_sample


#별칭
app_name = 'samples'


urlpatterns = [
    path('', TemplateView.as_view(template_name=app_name + '/index.html'), name='index'),
    path('<int:sample_no>', goto_sample, name='goto_sample'),
    path('capture_page', capture_page, name='capture_page'),
    path('fileupload', upload_file, name='upload_file'),
    path('fileupload2', upload_file2, name='fileupload2'),
    #path('fileupload2/<str:image_name>', read_uploaded_file, name='file_view'),
    path('add_sampledoc', add_sampledoc, name='add_sampledoc'),
    path('get_sampledoc', get_sampledoc, name='get_sampledoc'),
]

#path('upload/', views.upload_file, name='upload_file'),
#path('upload/success/', views.upload_success, name='file_upload_success')