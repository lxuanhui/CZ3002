# Generated by Django 3.2.5 on 2021-11-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=40, null=True),
        ),
    ]
