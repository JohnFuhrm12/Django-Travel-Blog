# Generated by Django 4.0.3 on 2022-04-04 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentBuenosAires',
        ),
        migrations.DeleteModel(
            name='CommentRiviera',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment'),
        ),
    ]
