# Generated by Django 2.2.7 on 2019-11-29 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]