# Generated by Django 5.1.5 on 2025-02-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchEntry', '0004_matchentry_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchentry',
            name='gender',
            field=models.CharField(default='Male', max_length=128),
            preserve_default=False,
        ),
    ]
