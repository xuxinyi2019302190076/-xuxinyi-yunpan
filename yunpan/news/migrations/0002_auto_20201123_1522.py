# Generated by Django 3.1.2 on 2020-11-23 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('attach', models.FileField(upload_to='')),
                ('remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '其他')])),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.student'),
        ),
    ]
