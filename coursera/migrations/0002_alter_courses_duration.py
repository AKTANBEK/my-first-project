# Generated by Django 3.2 on 2021-04-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='duration',
            field=models.CharField(max_length=15),
        ),
    ]