# Generated by Django 3.2.8 on 2021-10-31 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211031_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='article_unv',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.article')),
                ('articleAuthor', models.CharField(max_length=100, verbose_name='Author of this Article')),
            ],
            bases=('articles.article',),
        ),
    ]
