# Generated by Django 3.0.4 on 2020-03-21 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200321_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Organizer', 'verbose_name_plural': 'Organizers'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
    ]
