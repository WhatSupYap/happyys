from django.db import models
#import json

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
    
class SampleDoc(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
    
class UploadFile(models.Model):
    sampledoc = models.ForeignKey(SampleDoc, on_delete=models.CASCADE)
    idx = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/')
    original_file_name = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name
    

#upload_files = UploadFile.objects.filter(idx=0).select_related('sampledoc')
#for upload_file in upload_files:
#upload_files = UploadFile.objects.filter(idx=0).select_related('sampledoc')[:10]
#for upload_file in upload_files:
#    print(upload_file.sampledoc.title, upload_file.file)




