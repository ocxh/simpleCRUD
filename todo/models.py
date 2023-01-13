from django.db import models
from django.core.validators import MinLengthValidator

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    done = models.BooleanField(default=False)
    writer = models.CharField(max_length=20)