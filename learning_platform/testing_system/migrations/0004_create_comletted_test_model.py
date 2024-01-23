# Generated by Django 4.2.5 on 2023-10-10 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0003_create_teacher_group_model"),
        ("testing_system", "0003_create_article_answer_option_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompletedTest",
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
                    "test_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="testing_system.test",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorship.student",
                    ),
                ),
            ],
        ),
    ]