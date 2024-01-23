# Generated by Django 4.2.5 on 2023-10-10 15:39

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0002_create_teacher_model"),
        ("studying", "0001_create_specification_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Course")),
                (
                    "creater_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorship.teacher",
                    ),
                ),
                (
                    "specification_id",
                    models.ManyToManyField(to="studying.specification"),
                ),
            ],
            bases=(users.models.DateTimeMixin, models.Model),
        ),
    ]
