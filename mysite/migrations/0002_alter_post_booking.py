# Generated by Django 4.2.5 on 2023-11-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="booking",
            field=models.CharField(
                choices=[
                    ("In Library", "館藏中"),
                    ("Reserverd", "預約中"),
                    ("On load", "外借中"),
                ],
                default="In Library",
                max_length=20,
            ),
        ),
    ]
