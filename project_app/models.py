from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
  project_name=models.CharField(max_length=50)
  project_description = models.TextField()
  project_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return self.project_name 
  

