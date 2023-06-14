# Generated by Django 4.2.1 on 2023-05-30 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reste', '0006_blog_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='reviews',
        ),
        migrations.AddField(
            model_name='reviews',
            name='reviews',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reste.blog'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='comment',
            field=models.TextField(default='Good'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(default='Amir', max_length=100),
            preserve_default=False,
        ),
    ]
