from rest_framework import serializers
from .models import Account
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = Account
        fields = ('nickname', 'password')


    def create(self, validated_data):
        user = Account.objects.create_user(
            nickname=validated_data['nickname'],
            password=validated_data['password'],
        )
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(
        required = True,
        write_only = True
    )
    password = serializers.CharField(
        required = True,
        write_only = True,
    )
    class Meta(object):
        model = Account
        fields = ('nickname', 'password')

    def validate(self, data):
        nickname = data.get('nickname',None)
        password = data.get('password',None)

        if Account.objects.filter(nickname=nickname).exists():
            user = Account.objects.get(nickname=nickname)

            if not user.check_password(password):
                raise serializers.ValidationError('Check Your Email or Password')
        
        else:
            raise serializers.ValidationError("User does not exist")
        

        token = Token.objects.get(user=user)
        
        return str(token)