# Generated by Django 5.0.7 on 2024-08-08 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isg', '0002_rename_description_monster_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='sogsag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]