# Generated by Django 4.1.5 on 2023-07-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tech_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech_img',
            name='img',
            field=models.ImageField(upload_to='myapp/static/img'),
        ),
    ]
