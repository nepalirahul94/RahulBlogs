from django.db import models
from autoslug import AutoSlugField
from tinymce import models as tinymce_models


class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_author = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    blog_details = tinymce_models.HTMLField()
    slug = AutoSlugField(populate_from ='blog_title', 
           unique= True, null= True, default= None)

    def __str__(self):
        return self.blog_title

class Contact(models.Model):
    c_name = models.CharField(max_length = 50)
    c_email = models.EmailField()
    c_phone = models.IntegerField()
    c_message =models.TextField(max_length=300)

    def __str__(self):
        return self.c_message


