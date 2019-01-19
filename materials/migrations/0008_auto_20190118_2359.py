# Generated by Django 2.1.5 on 2019-01-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0007_delete_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handout',
            name='definitions_order',
        ),
        migrations.RemoveField(
            model_name='handout',
            name='word_order',
        ),
        migrations.AddField(
            model_name='handout',
            name='score',
            field=models.TextField(default='not provided'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='handout',
            name='title',
            field=models.TextField(default='not provided'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='handout',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='handout',
            name='user',
            field=models.TextField(default='not provided'),
            preserve_default=False,
        ),
    ]
