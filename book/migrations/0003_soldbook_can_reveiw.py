# Generated by Django 4.2.9 on 2024-02-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_soldbook_balance_after_buy_soldbook_timestmp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldbook',
            name='can_reveiw',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
