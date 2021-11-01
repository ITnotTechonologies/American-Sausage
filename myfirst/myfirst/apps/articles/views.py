from django.shortcuts import render

from .models import Article, article_unv, article_toefl, article_tal, article_sc

from django.http import Http404,HttpResponseRedirect

def index(request):
	latest_articles_list = Article.objects.order_by('-pubDate')[:5]
	return render(request, 'articles/main.html', {'latest_articles_list':latest_articles_list})


def speakingClub(request):
	articles_sc = article_sc.objects.all()
	return render(request, 'articles/speakingClub.html', {'articles_sc':articles_sc})

def detail(request, articleId):
	try:
		a = Article.objects.get( id = articleId)
	except:
		raise Http404("Article doesn't found")

	return render(request, 'articles/detail.html', {'article':a})


def tal(request):
	articles_tal = article_tal.objects.order_by('-pubDate')
	return render(request, 'articles/tal.html', {'articles_tal':articles_tal})

def detail_tal(request, article_tal_id):
	try:
		a = article_tal.objects.get( id = article_tal_id)
	except:
		raise Http404("")

	return render(request, 'articles/detail.html', {'article':a})


def toefl(request):
	articles_toefl = article_toefl.objects.order_by('-pubDate')
	return render(request, 'articles/TOEFL.html', {'articles_toefl':articles_toefl})

def detail_toefl(request, article_toefl_id):
	try:
		a = article_toefl.objects.get( id = article_toefl_id)
	except:
		raise Http404("")

	return render(request, 'articles/detail.html', {'article':a})


def unv(request):
	articles_unv = article_unv.objects.order_by('-pubDate')
	return render(request, 'articles/unv.html', {'articles_unv':articles_unv})


def detail_unv(request, article_unv_id):
	try:
		a = article_unv.objects.get( id = article_unv_id)
	except:
		raise Http404("")

	return render(request, 'articles/detail.html', {'article':a})