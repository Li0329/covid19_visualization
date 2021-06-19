# Generated by Django 3.2.3 on 2021-06-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0002_auto_20210612_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='China',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=250)),
                ('confirmed', models.IntegerField()),
                ('curConfirmed', models.IntegerField()),
                ('died', models.IntegerField()),
                ('cured', models.IntegerField()),
                ('confirmedRelative', models.IntegerField()),
            ],
        ),
    ]