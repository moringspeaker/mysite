# from rest_framework import serializers
# from .models import Users
#
# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('username', 'email','password')



from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class UserRegSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.set_email(validated_data['email'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ['id','username','email','password','level']