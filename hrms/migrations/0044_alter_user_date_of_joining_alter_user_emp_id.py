# Generated by Django 4.1.7 on 2023-06-06 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("hrms", "0043_alter_user_designation_alter_user_emp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="Date_of_joining",
            field=models.DateField(
                default=django.utils.timezone.now,
                help_text="Please choose a date",
                verbose_name="Select a date",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="emp_id",
            field=models.CharField(default="emp122", max_length=70),
        ),
    ]
