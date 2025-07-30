from django.db import models

# Create your models here.

from django.db import models

class File(models.Model):
  name = models.CharField(max_length=255)
  model = models.CharField(max_length=255)
  model_id = models.IntegerField()
  path_file = models.CharField(max_length=355)
  url_file = models.CharField(max_length=355)
  ext = models.CharField(max_length=255)
