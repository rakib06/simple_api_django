# Generated by Django 2.0 on 2022-05-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadith', '0002_auto_20220521_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hadith',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hadith',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete='SET_NULL', related_name='children', to='hadith.Hadith'),
        ),
    ]
