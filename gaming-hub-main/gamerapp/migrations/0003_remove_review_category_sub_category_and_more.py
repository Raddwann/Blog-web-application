# Generated by Django 4.2.9 on 2024-01-26 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamerapp', '0002_remove_review_intro_remove_review_outro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='category',
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('main_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gamerapp.category')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gamerapp.sub_category'),
        ),
    ]
