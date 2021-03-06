# Generated by Django 3.0.3 on 2020-03-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200302_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('which_laptop', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('model', models.CharField(max_length=150, null=True)),
                ('ram', models.CharField(max_length=150, null=True)),
                ('rom', models.CharField(max_length=150, null=True)),
                ('battery', models.CharField(max_length=150, null=True)),
                ('sales_package', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(max_length=150, null=True)),
                ('os', models.CharField(max_length=150)),
                ('l_type', models.CharField(max_length=150)),
                ('processor_type', models.CharField(max_length=150)),
                ('processor_generation', models.CharField(max_length=150)),
            ],
        ),
    ]
