# Generated by Django 4.2.5 on 2023-09-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('kelas', models.CharField(default='', max_length=255)),
                ('menu', models.CharField(default='', max_length=255)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.CharField(default='', max_length=255)),
                ('category', models.TextField()),
                ('date_added', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
