# Generated by Django 2.2.4 on 2020-05-06 09:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp1_questionnaire', '0002_remove_player_gained_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gained_amount',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
