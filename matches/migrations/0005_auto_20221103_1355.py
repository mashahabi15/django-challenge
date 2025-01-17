# Generated by Django 3.2.16 on 2022-11-03 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0003_alter_stadium_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0004_matchseat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchseat',
            options={'verbose_name': 'match_seats', 'verbose_name_plural': 'match_seats'},
        ),
        migrations.AlterField(
            model_name='matchseat',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_seats', to='matches.match'),
        ),
        migrations.AlterField(
            model_name='matchseat',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigner_seats', to='stadiums.seat'),
        ),
        migrations.AlterField(
            model_name='matchseat',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_matches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='matchseat',
            table='match_seat',
        ),
    ]
