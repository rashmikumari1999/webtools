from django.db import models

# Create your models here.
class Tools(models.Model):
    tools_id=models.AutoField
    tools_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
