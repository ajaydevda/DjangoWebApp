from django.db import models

# Create your models here.
class Webcontent(models.Model):

   webTextContent = models.CharField(max_length = 50)
 

   class Meta:
      db_table = "WebContentDataTable"