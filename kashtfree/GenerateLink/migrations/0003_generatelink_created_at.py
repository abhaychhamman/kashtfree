# Generated by Django 4.0.5 on 2023-02-15 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenerateLink', '0002_datacolumn_data10_datacolumn_data11'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatelink',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
