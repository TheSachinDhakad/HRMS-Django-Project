# Generated by Django 2.2.13 on 2023-03-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0013_auto_20230314_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='wh',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='emp_id',
            field=models.CharField(default='emp800', max_length=70),
        ),
    ]
