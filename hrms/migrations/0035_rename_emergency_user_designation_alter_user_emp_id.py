# Generated by Django 4.1.7 on 2023-03-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0034_alter_user_emp_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="emergency",
            new_name="designation",
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp928", max_length=70),
        ),
    ]
