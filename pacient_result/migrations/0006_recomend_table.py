# Generated by Django 3.0.2 on 2020-06-04 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacient_result', '0005_auto_20200530_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomend_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_text', models.DateTimeField(default='CURRENT_TIMESTAMP')),
                ('pacient', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
