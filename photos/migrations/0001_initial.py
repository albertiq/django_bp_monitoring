# Generated by Django 3.0.2 on 2020-03-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.CharField(default='DEFAULT VALUE', max_length=120)),
                ('name', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]