# Generated by Django 5.1.1 on 2024-09-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_chat_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='entities',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
