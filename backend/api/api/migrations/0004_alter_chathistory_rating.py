# Generated by Django 4.2.5 on 2023-11-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_chathistory_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chathistory",
            name="rating",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
