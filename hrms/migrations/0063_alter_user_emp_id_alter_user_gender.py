# Generated by Django 4.2.1 on 2023-06-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0062_user_gender_alter_user_emp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp910", max_length=70),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "MALE"), ("female", "FEMALE"), ("other", "OTHER")],
                default=False,
                max_length=15,
            ),
        ),
    ]