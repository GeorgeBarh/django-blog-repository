# Generated by Django 4.2.18 on 2025-04-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_post_field_2_post_field_3_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
        migrations.AddField(
            model_name='comment',
            name='new_field',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
