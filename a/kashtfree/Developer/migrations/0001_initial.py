# Generated by Django 4.0.5 on 2023-02-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('github', models.TextField()),
                ('insta', models.TextField()),
                ('linkedin', models.TextField()),
                ('desc', models.TextField()),
                ('skills', models.TextField()),
            ],
        ),
    ]