# Generated by Django 4.1.7 on 2023-06-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0047_alter_user_emp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp700", max_length=70),
        ),
    ]