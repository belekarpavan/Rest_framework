# Generated by Django 2.1 on 2018-08-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180818_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
