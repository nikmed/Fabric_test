from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions         
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .models import Poll, Question, Answer
from .serializer import PollSerializer, QuestionSerializer, AnswerSerializer
from datetime import datetime



class PollView(ListCreateAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer
	permission_classes = (permissions.IsAdminUser,)

class ActivePollView(ListAPIView):
	queryset = Poll.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())
	serializer_class = PollSerializer


class SinglePollView(RetrieveUpdateDestroyAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer
	permission_classes = (permissions.IsAdminUser,)
		

class QuestionView(ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = (permissions.IsAdminUser,)


class SingleQuestionView(RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = (permissions.IsAdminUser,)


class AnswerView(ListCreateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class ListAnswerView(ListAPIView):
	serializer_class = AnswerSerializer
	def get_queryset(self):
		return Answer.objects.filter(user_id=self.kwargs['user_id'])
