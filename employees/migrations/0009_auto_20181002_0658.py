# Generated by Django 2.1.1 on 2018-10-02 06:58

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20181002_0631'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='amendmentrequest',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='applicationrequest',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='assessment',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='idrequest',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='returnsrequest',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
