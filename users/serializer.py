from rest_framework import serializers
from .models import User, Condition

class UserSerializer(serializers.ModelSerializer):
    # phone = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True,)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password',]

    def create(self, validated_data):

        phone = validated_data['phone']
        password = validated_data['password']
        # validated_data.pop('password')
        # validated_data.pop('phone')
        print(validated_data)

        user = User.objects.create_user( **validated_data)
        # password = validated_data['password']
        # user = create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.desc = validated_data.get('desc', instance.desc)
    #     instance.save()
    #     return instance