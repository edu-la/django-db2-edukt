from rest_framework import serializers
from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id', 'username', 'email')  # email


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'subscription', 'university', 'school')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        subscriber = Subscriber.objects.create_user(**validated_data)
        return subscriber


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('username', 'password')
