# Generated by Django 2.0 on 2022-05-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadith', '0004_auto_20220521_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hadith',
            name='subtitle',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='hadith',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
