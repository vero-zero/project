# Generated by Django 4.2 on 2023-04-29 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_remove_user_id_alter_user_nickname"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"managed": True},
        ),
        migrations.AlterModelTable(
            name="user",
            table="User",
        ),
    ]