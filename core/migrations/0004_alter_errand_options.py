# Generated by Django 4.2 on 2023-04-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_errand_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errand',
            options={'ordering': ['completed']},
        ),
    ]