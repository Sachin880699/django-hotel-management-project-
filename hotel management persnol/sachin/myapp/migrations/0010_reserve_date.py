# Generated by Django 2.2.1 on 2019-05-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20190515_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='date',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
    ]
