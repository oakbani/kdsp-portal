# Generated by Django 3.2.7 on 2021-09-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queues", "0002_auto_20210918_1956"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list",
            name="status",
            field=models.IntegerField(choices=[(1, "Pending"), (2, "Done")], default=1),
        ),
    ]
