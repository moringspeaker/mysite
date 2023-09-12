# from rest_framework import serializers
# from .models import Users
#
# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('username', 'email','password')



from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from.models import UserProfile

User = get_user_model()
class UserRegSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.email = validated_data['email']
        user.level = 1
        user.save()
        return user
    class Meta:
        model = User
        fields = ['id','username','email','password','level']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])

        if user and user.is_active:
            # Check if the user's level is as per your requirements
            if user.level == UserProfile.LEVEL[0][0] or user.level == UserProfile.LEVEL[1][0]:
                return user
            else:
                raise serializers.ValidationError("User level is not valid for login")
        else:
            raise serializers.ValidationError("Incorrect Credentials")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','level']