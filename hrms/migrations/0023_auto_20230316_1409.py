# Generated by Django 2.2.13 on 2023-03-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0022_auto_20230316_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emp_id',
            field=models.CharField(default='emp611', max_length=70),
        ),
    ]
