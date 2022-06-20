from asyncore import write
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )


    password = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
        )
    password_confirmation = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        style={'input_type': 'password'}
        )

    

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password":"Passwords don't match"})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


        # user = User.objects.create(
        #     username=validated_data['username'],
        #     email=validated_data['email'],
        #     )
        # user.set_password(validated_data['password'])
        # user.save()
        # return user


