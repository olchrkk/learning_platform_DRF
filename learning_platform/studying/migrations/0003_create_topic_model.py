# Generated by Django 4.2.5 on 2023-10-10 15:43

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("studying", "0002_create_course_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                (
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Topic name"
                    ),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studying.course",
                    ),
                ),
            ],
            bases=(users.models.DateTimeMixin, models.Model),
        ),
    ]