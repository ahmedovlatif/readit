# Generated by Django 4.2.1 on 2023-06-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(max_length=211, null=True),
        ),
    ]
