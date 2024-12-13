# Generated by Django 5.1.4 on 2024-12-18 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamerapp", "0018_blog_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog_post",
            name="main_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gamerapp.category",
            ),
        ),
        migrations.AlterField(
            model_name="blog_post",
            name="sub_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gamerapp.sub_category",
            ),
        ),
        migrations.AlterField(
            model_name="blog_post",
            name="sub_subcategory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gamerapp.sub_subcategory",
            ),
        ),
    ]
