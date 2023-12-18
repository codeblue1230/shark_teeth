# Generated by Django 4.2.7 on 2023-11-30 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_forum"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="forum",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="main.forum"
            ),
            preserve_default=False,
        ),
    ]