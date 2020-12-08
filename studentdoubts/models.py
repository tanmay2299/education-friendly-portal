from django.db import models

# Create your models here.
class account(models.Model):
    student_name = models.CharField(max_length=100)
    parent_name =models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    subject =models.CharField(max_length=100)
    time=models.CharField(max_length=200)
class contents(models.Model):
    subject=models.CharField(max_length=11)
    topic=models.CharField(max_length=101)
    topic_info=models.CharField(max_length=1000)
    links=models.URLField(max_length=100)    
    

