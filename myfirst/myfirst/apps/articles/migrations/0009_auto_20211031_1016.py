# Generated by Django 3.2.8 on 2021-10-31 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_tal_article_toefl'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article_tal',
            options={'verbose_name': 'Статья с полезными советами и лайфхаками', 'verbose_name_plural': 'Статьи с полезными советами и лайфхаками'},
        ),
        migrations.AlterModelOptions(
            name='article_toefl',
            options={'verbose_name': 'Статья о TOEFL', 'verbose_name_plural': 'Статьи о TOEFL'},
        ),
        migrations.AlterModelOptions(
            name='article_unv',
            options={'verbose_name': 'Статья о поступлении', 'verbose_name_plural': 'Статьи о поступлении'},
        ),
    ]
