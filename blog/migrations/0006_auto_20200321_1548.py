# Generated by Django 2.2.7 on 2020-03-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_message_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='byline',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='https://images.unsplash.com/photo-1584713284836-873df2d32409?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('DR', 'Descriptions'), ('NA', 'Nature'), ('TH', 'Threshold'), ('E', 'Experiences'), ('SC', 'School')], default='SC', max_length=2),
        ),
    ]
