from django.db import models

# Create your models here.


class Photo(models.Model):
    image_id = models.CharField(max_length=120, default='DEFAULT VALUE')
    name = models.ImageField(null=True)

    def __str__(self):
        return self.image_id
