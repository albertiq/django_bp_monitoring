from django.db import models
from django.utils.timezone import now
# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Pacient_table(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.TextField()
    date_ad = models.DateTimeField(default='CURRENT_TIMESTAMP')
    username = models.TextField(default='')
    slug = models.SlugField(default='')
    user_id = models.ForeignKey(User, to_field = "id", on_delete=models.CASCADE,default='')

class Recomend_table(models.Model):
    id = models.AutoField(primary_key=True)
    pacient = models.ForeignKey(User, to_field = "id", on_delete=models.CASCADE,default='')
    text = models.TextField()
    date_text = models.DateTimeField(default=now)



