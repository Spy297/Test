# Generated by Django 4.2.2 on 2023-06-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]