# Generated by Django 2.2 on 2019-05-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0004_auto_20190520_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='link',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='shops',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='category',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='link',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='shops',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
