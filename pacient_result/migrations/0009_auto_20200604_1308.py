# Generated by Django 3.0.2 on 2020-06-04 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacient_result', '0008_auto_20200604_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomend_table',
            name='pacient',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pacient_result.Pacient_table'),
        ),
    ]
