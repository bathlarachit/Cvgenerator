# Generated by Django 3.0.3 on 2020-08-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_cv_cvname'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='degree',
            field=models.CharField(default='B.tech', max_length=360),
        ),
    ]