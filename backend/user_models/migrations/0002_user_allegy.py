# Generated by Django 4.0.1 on 2022-02-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allegy',
            field=models.CharField(max_length=100, null=True),
        ),
    ]