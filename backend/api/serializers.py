from rest_framework import serializers
from .models import People, Vehicle, Ownership


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'first_name', 'last_name', 'address', 'license', 'dob']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class OwnershipSerializer(serializers.ModelSerializer):
    people = PeopleSerializer()
    vehicle = VehicleSerializer()

    class Meta:
        model = Ownership
        fields = '__all__'

    def create(self, validated_data):
        people_data = validated_data.pop('people')
        vehicle_data = validated_data.pop('vehicle')
        print(people_data)
        # check if a people instance with the same detail exists
        people_instance = People.objects.filter(
            first_name=people_data['first_name'],
            last_name=people_data['last_name'],
            address=people_data['address'],
            dob=people_data['dob'],
            license=people_data['license']
        ).first()

        if people_instance:
            people = people_instance
            print('people already exist')
        else:
            print('creating new people')
            people = People.objects.create(**people_data)

        vehicle = Vehicle.objects.create(**vehicle_data)

        ownership = Ownership.objects.create(
            people=people, vehicle=vehicle, **validated_data)

        return ownership
