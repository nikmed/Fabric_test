from re import S
from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator

QUESTION_TYPE_CHOICES = [
	('TXT', 'Text answer'), 
	('POA' , 'Pick one answer'), 
	('PMA' , 'Pick multiple answer'),
	]


class Poll(models.Model):
	"""Опрос"""
	name = models.CharField(max_length=255)
	start_date = models.DateField(auto_now_add=True)
	end_date = models.DateField(default=datetime.now().date() + timedelta(days=1))
	description = models.TextField()

	def __str__(self):
		return str(self.name)


class Question(models.Model):
	"""Вопрос"""
	text = models.TextField()
	answer = models.CharField(max_length=255)
	question_type = models.CharField(
		max_length=3,
		choices=QUESTION_TYPE_CHOICES,
		default='TXT',
		)
	poll = models.ForeignKey('Poll', related_name='poll', on_delete=models.CASCADE)

	def __str__(self):
		return self.text


class Answer(models.Model):
	"""Ответ"""
	user_id = models.IntegerField(validators=[
            MinValueValidator(0)
        ])
	question_id = models.ForeignKey('Question', related_name='question', on_delete=models.CASCADE)
	answer = models.CharField(max_length=255) 
	correct = models.BooleanField(default=False)
	def __str__(self):
		return self.answer
	def is_correct(self):
		if self.question_id.question_type != 'PMA':
			self.correct = (self.answer == self.question_id.answer)
			self.save()
		else:
			answers = sorted(list(map(int, self.answer.split(' '))))
			correct_answers = sorted(list(map(int, self.question_id.answer.split(' '))))
			self.correct = (answers == correct_answers)
			self.save()
		return self.correct

