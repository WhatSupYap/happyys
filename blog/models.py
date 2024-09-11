from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Image(models.Model):
    orginal_file_name = models.TextField()
    thumbnail_path = models.TextField(null=True)
    # 이미지 경로를 images/연월일_랜덤문자열_파일명 형식으로 저장 하는게 좋을지도
    uploaded_path = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.orginal_file_name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sort = models.IntegerField() # 추가 20240912
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


# Create your models here.
class Post(models.Model):
    """
    id
    제목 
    내용
    작성일
    수정일
    이미지
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(Image, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    # 카테고리 추가는 맞는데 on_delete=models.CASCADE는 아닌 것 같다. 근데 필수다
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', default=0)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_yn = models.CharField(max_length=1, default='Y')
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
    
# 백업은 나중에
# class Post_backup(models.Model):
#     """
#     id
#     제목 
#     내용
#     작성일
#     수정일
#     이미지
#     """
#     id = models.AutoField(primary_key=True)
#     ref_id = models.IntegerField()
#     revision = models.IntegerField()
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     images = models.ManyToManyField(Image, related_name='posts')
#     tags = models.ManyToManyField(Tag, related_name='posts')

#     def __str__(self):  # __unicode__ on Python 2
#         return self.title

class Reply(models.Model):
    """
    id
    내용
    작성일
    수정일
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_yn = models.CharField(max_length=1, default='Y')
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.content