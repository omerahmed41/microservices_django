# Generated by Django 3.0.1 on 2020-01-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_todoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='createDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='expireDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='flag',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.TextField(),
        ),
    ]
