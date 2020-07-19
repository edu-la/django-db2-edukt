from rest_framework import serializers

from questionnaire.models import Questionnaire, Question, Alternative


class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = ['description', 'correct_alt']


class QuestionSerializer(serializers.ModelSerializer):
    alternatives = AlternativeSerializer(many=True)

    class Meta:
        model = Question
        fields = ['description', 'alternatives']


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, write_only=True)

    class Meta:
        model = Questionnaire
        fields = ['id', 'course', 'topic', 'questions']

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        questionnaire = Questionnaire.objects.create(**validated_data)
        questionnaire.save()

        for question in questions:
            q = Question.objects.create(questionnaire=questionnaire, description=question['description'])
            for alternative in question['alternatives']:
                Alternative.objects.create(question_id=q.id, **alternative)

        return questionnaire


class QuestionnaireHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Questionnaire
        fields = ['url']
