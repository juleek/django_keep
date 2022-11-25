from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Note(models.Model):
    description = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    subject = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
