# Generated by Django 4.2.4 on 2023-08-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0002_rename_subscriber_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscribe_news',
            field=models.BooleanField(default=True),
        ),
    ]