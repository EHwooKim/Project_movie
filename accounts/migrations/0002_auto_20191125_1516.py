# Generated by Django 2.2.7 on 2019-11-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preference',
            field=models.ManyToManyField(blank=True, related_name='preferences', to='movies.Genre'),
        ),
    ]