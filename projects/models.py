from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Relation Works 
class Works (models.Model):
    Project_title = models.CharField(max_length = 100) # The title of the project is stored here 
    About_project = models.TextField() # a brief explanation of what the project is about
    date_posted = models.DateTimeField(default = timezone.now) # The date which the project is registered in the database

    class Meta:
        verbose_name_plural = "Works" 

    def __str__(self):
        return self.Project_title    # this method ensures th ateach entry is recognised by its title on the admin page

