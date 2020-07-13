from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone_no', 'created_by', 'group', 'status')
        extra_kwargs = {
            'password' : {'write_only' : True}
        }