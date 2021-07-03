from django.db import models
from django.db.models.base import Model

# Create your models here.
# class usercreate(models.Model):
#     user_name=models.CharField(max_length=100)
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)
#     email_id=models.EmailField(max_length=100)
#     user_password=models.CharField(max_length=100)

#     def __str__(self):
#         return self.user_name
class form_info(models.Model):
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    contacts=models.CharField(max_length=100)
    contacts_ext=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images', null=True,blank=True)
    team=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    join_date=models.DateTimeField(blank=True, null=True)
    last_date=models.DateTimeField(blank=True, null=True)
    email_id=models.EmailField(max_length=100)
    titleof=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

       