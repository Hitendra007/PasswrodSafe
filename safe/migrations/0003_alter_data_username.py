# Generated by Django 4.2.2 on 2023-07-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0002_data_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='username',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
