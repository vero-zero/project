# Generated by Django 4.2 on 2023-04-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="user",
            table="User",
        ),
    ]
