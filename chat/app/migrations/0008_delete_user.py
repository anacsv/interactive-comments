# Generated by Django 4.1.1 on 2022-09-16 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_user_created_by_user_created_date_user_date_joined_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
