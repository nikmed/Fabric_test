from django.urls import path
from .views import PollView, ActivePollView, SinglePollView, QuestionView, SingleQuestionView, AnswerView, ListAnswerView


app_name = "polls"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
	path('poll/', PollView.as_view()),
	path('poll/<int:pk>', SinglePollView.as_view()),
	path('acitve_poll/', ActivePollView.as_view()),
	path('question/', QuestionView.as_view()),
	path('question/<int:pk>', SingleQuestionView.as_view()),
	path('answer/', AnswerView.as_view()),
	path('answer/<int:user_id>', ListAnswerView.as_view())
	]