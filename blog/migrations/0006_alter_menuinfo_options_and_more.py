# Generated by Django 5.0.1 on 2024-02-15 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_menuinfo_options_menuinfo_priority_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuinfo',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='menuinfo',
            name='blog_menuin_priorit_7329a7_idx',
        ),
    ]