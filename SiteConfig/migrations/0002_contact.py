# Generated by Django 3.2.10 on 2022-01-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteConfig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(default='请填入HTML格式文字')),
            ],
        ),
    ]
