# Generated by Django 2.1 on 2018-08-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]
