# Generated by Django 4.1.3 on 2023-01-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qst',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('questionImage', models.ImageField(blank=True, null=True,
                 upload_to='quiz_images', verbose_name='Question picture')),
                ('answerText', models.CharField(
                    max_length=100, verbose_name='Question text')),
                ('isCorrect', models.BooleanField(verbose_name='Correct')),
            ],
            options={
                'verbose_name': 'Qst',
                'verbose_name_plural': 'Qsts',
            },
        ),
    ]
