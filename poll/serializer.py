from rest_framework import serializers
from .models import Poll, Answer, Question


class PollSerializer(serializers.Serializer):
	id = serializers.PrimaryKeyRelatedField(read_only=True)
	name = serializers.CharField(max_length=255)
	start_date = serializers.DateField(required=False, read_only=True)
	end_date = serializers.DateField(required=False)
	description = serializers.CharField(max_length=255)

	def create(self, validated_data):
		return Poll.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.end_date = validated_data.get('end_date', instance.end_date)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		return instance



class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = [
		'id',
		'text',
		'question_type',
		'poll'
		]
		


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = [
		'id',
		'user_id',
		'question_id',
		'answer'
		]
		read_only_fields = [
		'id'
		] 

