from rest_framework import serializers
from .models import Incident, Offense, People, Vehicle, Ownership
from django.contrib.auth.models import User


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'first_name', 'last_name', 'address', 'license', 'dob']
        extra_kwargs = {'license': {
            'validators': []
        }}


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class OwnershipSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(required=False, allow_null=True)
    vehicle = VehicleSerializer(required=False, allow_null=True)

    class Meta:
        model = Ownership
        fields = '__all__'


class OffenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offense
        fields = ['__all__']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class IncidentSerializer(serializers.ModelSerializer):
    ownership = OwnershipSerializer()
    offense = serializers.PrimaryKeyRelatedField(queryset=Offense.objects.all())
    # creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Incident
        fields = '__all__'
