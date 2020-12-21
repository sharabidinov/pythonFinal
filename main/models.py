from django.db import models


class Task(models.Model):
	title = models.CharField('Имя', max_length=50)
	task = models.TextField('Информация')

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Поздравление'
		verbose_name_plural = 'Поздравления'

class Info(models.Model):
	title = models.CharField('имя', max_length=50)
	task = models.TextField('Информация')

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Информация'
		verbose_name_plural = 'Информация'