# Generated by Django 5.0.7 on 2024-07-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('isDeleted', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='LobbyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobby', models.CharField(max_length=20)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=40)),
                ('isDeleted', models.IntegerField(max_length=1)),
                ('isActive', models.IntegerField(max_length=1)),
                ('order', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='brandinfo',
            name='favicon',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='brandinfo',
            name='heroLogo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
