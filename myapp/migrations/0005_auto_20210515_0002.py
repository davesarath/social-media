# Generated by Django 3.0.2 on 2021-05-14 18:32

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200430_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custmodel',
            name='pro_pic',
            field=models.FileField(null=True, upload_to=myapp.models.path_and_rename),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='img',
            field=models.FileField(blank=True, upload_to='post'),
        ),
    ]
