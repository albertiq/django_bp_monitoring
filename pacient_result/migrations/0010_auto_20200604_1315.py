# Generated by Django 3.0.2 on 2020-06-04 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacient_result', '0009_auto_20200604_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomend_table',
            name='pacient',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]