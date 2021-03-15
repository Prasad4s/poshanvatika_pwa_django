# Generated by Django 3.1.5 on 2021-01-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('afifpartner', models.CharField(max_length=10)),
                ('afif', models.CharField(blank=True, max_length=10, null=True)),
                ('covervillage', models.IntegerField()),
                ('averagehousehold', models.IntegerField()),
                ('shg', models.IntegerField()),
            ],
        ),
    ]