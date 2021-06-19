# Generated by Django 3.2.3 on 2021-06-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='world',
            name='confirmed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='world',
            name='confirmedRelative',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='world',
            name='curConfirmed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='world',
            name='cured',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='world',
            name='died',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='world',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
