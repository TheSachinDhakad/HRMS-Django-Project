# Generated by Django 2.2.13 on 2023-03-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0016_auto_20230315_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emp_id',
            field=models.CharField(default='emp170', max_length=70),
        ),
    ]
