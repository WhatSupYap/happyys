from django.db import models

# Create your models here.
class Monster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    # 설명
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sogsag(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='images/')
    # 상태 : 등록(0), 처리됨(1), 삭제됨(2)
    status = models.IntegerField(default=0)
    # 타입 : 생각(0), 의문(1), 욕구(2), 아이디어(3), 할일(4), 기타(5)
    type = models.IntegerField(default=0)
    ref_id = models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True) # auto_now_add=True : 생성시간 자동 저장

    def __str__(self):
        return self.content


class Quest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    reward = models.CharField(max_length=50)
    #reward2 = models.CharField(max_length=50 , default='0')

    def __str__(self):
        return self.title
    
