# Generated by Django 2.2.4 on 2020-07-01 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exp1_questionnaire', '0006_auto_20200507_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='is_selected',
        ),
    ]
