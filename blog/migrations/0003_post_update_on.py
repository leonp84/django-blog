# Generated by Django 4.2.11 on 2024-04-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_excerpt_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
