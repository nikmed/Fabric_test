from django.contrib import admin
from .models import Poll, Question, Answer

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_id',
    'answer',
    'question_id',
    'correct',
    'is_correct')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id',
		'text',
		'answer',
		'question_type',
		'poll')

class PollAdmin(admin.ModelAdmin):
    list_display = ('id',
	'name',
	'start_date',
	'end_date',
	'description')
    fields = [
	'name',
    'description',
	('end_date'),
	]


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)