# Generated by Django 2.1.5 on 2019-01-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheretofindme', '0002_auto_20190108_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internetidentity',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
