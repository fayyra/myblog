# Generated by Django 4.0.6 on 2022-08-11 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_comment_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
