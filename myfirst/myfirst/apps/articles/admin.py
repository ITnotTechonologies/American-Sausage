from django.contrib import admin

# Register your models here.
from .models import Article, article_unv, article_tal, article_toefl, article_sc

admin.site.register(article_sc)
admin.site.register(Article)
admin.site.register(article_unv)
admin.site.register(article_toefl)
admin.site.register(article_tal)
