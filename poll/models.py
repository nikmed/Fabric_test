from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator


class Poll(models.Model):
	name = models.CharField(max_length=255)
	start_date = models.DateField(auto_now_add=True)
	end_date = models.DateField(default=datetime.now().date() + timedelta(days=1))
	description = models.TextField()

	def __str__(self):
		return str(self.id)


class Question(models.Model):
	QUESTION_TYPE_CHOICES = [
	('TXT', 'Text answer'), 
	('POA' , 'Pick one answer'), 
	('PMA' , 'Pick multiple answer'),
	]

	text = models.TextField()
	question_type = models.CharField(
		max_length=3,
		choices=QUESTION_TYPE_CHOICES,
		default='TXT',
		)
	poll = models.ForeignKey('Poll', related_name='poll', on_delete=models.CASCADE)

	def __str__(self):
		return self.text


class Answer(models.Model):
	user_id = models.IntegerField(validators=[
            MinValueValidator(0)
        ])
	question_id = models.ForeignKey('Question', related_name='question', on_delete=models.CASCADE)
	answer = models.CharField(max_length=255) 

	def __str__(self):
		return self.answer
