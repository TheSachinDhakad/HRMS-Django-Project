# Generated by Django 4.1.7 on 2023-06-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0044_alter_user_date_of_joining_alter_user_emp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="Designation",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp736", max_length=70),
        ),
    ]
