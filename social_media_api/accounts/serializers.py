from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Generate a token for the new user
        Token.objects.get_or_create(user=user)
        return user

    def get_token(self, obj):
        # Retrieve or create a token for the user
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def validate(self, data):
        from django.contrib.auth import authenticate

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        self.user = user
        return data

    def get_token(self, obj):
        # Retrieve or create a token for the authenticated user
        token, _ = Token.objects.get_or_create(user=self.user)
        return token.key