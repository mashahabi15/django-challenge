# Generated by Django 3.2.16 on 2022-11-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_rename_is_active_match_is_selling_ticket_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_duration',
            field=models.IntegerField(null=True),
        ),
    ]
