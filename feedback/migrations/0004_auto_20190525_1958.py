# Generated by Django 2.0.6 on 2019-05-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20190525_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
    ]
