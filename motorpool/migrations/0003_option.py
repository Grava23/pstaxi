# Generated by Django 4.0.2 on 2022-03-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0002_alter_brand_options_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Опции',
            },
        ),
    ]
