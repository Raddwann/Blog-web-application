# Generated by Django 5.1.4 on 2024-12-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamerapp", "0022_alter_blog_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog_post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
