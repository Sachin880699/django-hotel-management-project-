# Generated by Django 2.2.1 on 2019-05-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190515_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]