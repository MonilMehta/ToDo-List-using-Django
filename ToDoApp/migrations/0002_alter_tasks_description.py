# Generated by Django 4.2 on 2023-10-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ToDoApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="description",
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]