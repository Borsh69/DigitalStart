# Generated by Django 4.2.4 on 2023-12-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_comment_competitions_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitions',
            name='comment',
        ),
        migrations.AddField(
            model_name='project',
            name='comments',
            field=models.ManyToManyField(blank=True, to='base.comment'),
        ),
    ]
