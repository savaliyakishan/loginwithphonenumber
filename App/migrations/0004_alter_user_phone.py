# Generated by Django 4.2.1 on 2023-05-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(db_column='Phone_Number', max_length=10, unique=True),
        ),
    ]
