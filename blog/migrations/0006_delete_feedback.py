# Generated by Django 4.2.1 on 2023-06-05 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
