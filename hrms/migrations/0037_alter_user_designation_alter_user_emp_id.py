# Generated by Django 4.1.7 on 2023-03-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0036_alter_user_emp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="designation",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp816", max_length=70),
        ),
    ]
