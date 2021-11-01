import datetime

from django.db import models

from django.utils import timezone


class Article(models.Model):
	aTitle = models.CharField('Name of an Article', max_length = 50)
	aText = models.TextField('Text of an Article')
	pubDate = models.DateTimeField('Date of publication an Article')
	# AuthorName = models.CharField('Author of that Article', max_length = 50)
	def __str__(self):
		return self.aTitle
	def information(self):
		s1 = "Title of an Article: " + str(self.aTitle)
		s2 = "Text of an Article: " + str(self.aText)
		s3 = "Date of publication of an Article: " + str(self.pubDate)
		print(s1)
		print(s2)
		print(s3)
	

	def was_published_recently(self):
		return self.pubDate  >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'



class article_sc(models.Model):
	aTitle = models.CharField('Name of an Article', max_length = 50)
	aText = models.TextField('Text of an Article')
	pubDate = models.DateTimeField('Date of publication an Article')
	# AuthorName = models.CharField('Author of that Article', max_length = 50)
	def __str__(self):
		return self.aTitle
	def information(self):
		s1 = "Title of an Article: " + str(self.aTitle)
		s2 = "Text of an Article: " + str(self.aText)
		s3 = "Date of publication of an Article: " + str(self.pubDate)
		print(s1)
		print(s2)
		print(s3)
	

	def was_published_recently(self):
		return self.pubDate  >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья про спикинг клаб'
		verbose_name_plural = 'Статьи про спикинг клаб'

class article_unv(models.Model):
	aTitle = models.CharField('Name of an Article', max_length = 50)
	aText = models.TextField('Text of an Article')
	pubDate = models.DateTimeField('Date of publication an Article')
	# AuthorName = models.CharField('Author of that Article', max_length = 50)
	def __str__(self):
		return self.aTitle
	def information(self):
		s1 = "Title of an Article: " + str(self.aTitle)
		s2 = "Text of an Article: " + str(self.aText)
		s3 = "Date of publication of an Article: " + str(self.pubDate)
		print(s1)
		print(s2)
		print(s3)
	

	def was_published_recently(self):
		return self.pubDate  >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья о поступлении'
		verbose_name_plural = 'Статьи о поступлении'


class article_toefl(models.Model):
	aTitle = models.CharField('Name of an Article', max_length = 50)
	aText = models.TextField('Text of an Article')
	pubDate = models.DateTimeField('Date of publication an Article')
	# AuthorName = models.CharField('Author of that Article', max_length = 50)
	def __str__(self):
		return self.aTitle
	def information(self):
		s1 = "Title of an Article: " + str(self.aTitle)
		s2 = "Text of an Article: " + str(self.aText)
		s3 = "Date of publication of an Article: " + str(self.pubDate)
		print(s1)
		print(s2)
		print(s3)
	

	def was_published_recently(self):
		return self.pubDate  >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья о TOEFL'
		verbose_name_plural = 'Статьи о TOEFL'



class article_tal(models.Model):
	aTitle = models.CharField('Name of an Article', max_length = 50)
	aText = models.TextField('Text of an Article')
	pubDate = models.DateTimeField('Date of publication an Article')
	
	# AuthorName = models.CharField('Author of that Article', max_length = 50)
	def __str__(self):
		return self.aTitle
	def information(self):
		s1 = "Title of an Article: " + str(self.aTitle)
		s2 = "Text of an Article: " + str(self.aText)
		s3 = "Date of publication of an Article: " + str(self.pubDate)
		print(s1)
		print(s2)
		print(s3)
	

	def was_published_recently(self):
		return self.pubDate  >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья с полезными советами и лайфхаками'
		verbose_name_plural = 'Статьи с полезными советами и лайфхаками'