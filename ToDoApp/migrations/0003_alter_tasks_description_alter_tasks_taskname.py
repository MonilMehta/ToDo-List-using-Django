# Generated by Django 4.2 on 2023-10-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ToDoApp", "0002_alter_tasks_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="description",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="tasks",
            name="taskname",
            field=models.CharField(max_length=50),
        ),
    ]