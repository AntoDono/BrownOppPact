# Generated by Django 5.1.5 on 2025-02-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchEntry', '0007_matchentry_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchentry',
            name='permission_to_share',
            field=models.BooleanField(default=False),
        ),
    ]
