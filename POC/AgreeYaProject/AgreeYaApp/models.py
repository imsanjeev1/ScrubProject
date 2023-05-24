from django.db import models


class Record_data(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Email = models.EmailField(max_length=70, null=True, blank=True, unique=False)
    Filepath = models.CharField(max_length=500)
    class Meta:
        db_table = "data_tables"
# Create your models here.
