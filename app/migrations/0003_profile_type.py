# Generated by Django 4.1.7 on 2023-06-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_fisrt_name_profile_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]