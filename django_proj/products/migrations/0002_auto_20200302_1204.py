# Generated by Django 3.0.3 on 2020-03-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellphones',
            name='battery',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cellphones',
            name='color',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cellphones',
            name='front_camera',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cellphones',
            name='ram',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cellphones',
            name='rear_camera',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='cellphones',
            name='rom',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cellphones',
            name='model',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cellphones',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cellphones',
            name='price',
            field=models.IntegerField(),
        ),
    ]
