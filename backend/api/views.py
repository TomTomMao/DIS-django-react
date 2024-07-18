from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.models import Incident, Offense, Ownership, People, Vehicle
from api.serializers import IncidentSerializer, OwnershipSerializer, PeopleSerializer
from rest_framework.permissions import AllowAny
from django.db.models.functions import Concat
from django.db.models import Value, Q

# Create your views here.


class PeopleList(generics.ListAPIView):
    serializer_class = PeopleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = People.objects.all()
        name = self.request.query_params.get('name')
        license = self.request.query_params.get('license')
        if name is not None:
            if license is not None: # invalid search
                queryset = []
            elif name == '':
                queryset = People.objects.all()
            elif ' ' in name:  # full name search
                queryset = People.objects.annotate(
                    full_name=Concat('first_name', Value(' '), 'last_name')).filter(full_name__iexact=name)
            else: # partial name search
                queryset = People.objects.all().filter(
                    Q(first_name__iexact=name) | Q(last_name__iexact=name))
        elif license is not None:
            if name is not None: # invalid search
                queryset = []
            elif license == '':
                queryset = People.objects.all()
            else:
                queryset = People.objects.filter(license__iexact=license)
                
        return queryset

class OwnershipListCreate(generics.ListCreateAPIView):
    serializer_class = OwnershipSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Ownership.objects.all()
        plate_number = self.request.query_params.get('plate_number', None)
        if plate_number:
            queryset = queryset.filter(
                vehicle__plate_number__iexact=plate_number)

        return queryset

    def perform_create(self, serializer):
        people, created = get_or_create_people(self.request.data)
        vehicle, created = get_or_create_vehicle(self.request.data)

        serializer.save(people=people, vehicle=vehicle)


class IncidentListCreate(generics.ListCreateAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [AllowAny]
    queryset = Incident.objects.all()

    def perform_create(self, serializer):
        print(self.request.data)
        people, created_people = get_or_create_people(self.request.data)
        vehicle, created_vehicle = get_or_create_vehicle(self.request.data)
        ownership, created_ownership = Ownership.objects.get_or_create(
            vehicle=vehicle, people=people)
        offense = Offense.objects.get(id=self.request.data.get('offense'))
        date = self.request.data.get('date')
        report = self.request.data.get('report')
        serializer.save(ownership=ownership, offense=offense,
                        date=date, report=report)


def get_or_create_people(data):
    people_data = data.get('ownership').get('people')
    if people_data is None:
        people = None
        created = False
        print('people_data is none')
    else:
        people, created = People.objects.get_or_create(
            first_name=people_data['first_name'],
            last_name=people_data['last_name'],
            address=people_data['address'],
            dob=people_data['dob'],
            license=people_data['license']
        )
    return people, created


def get_or_create_vehicle(data):
    vehicle_data = data.get('ownership').get('vehicle')
    if vehicle_data is None:
        print('vehicle_data is none')
        vehicle = None
        created = False
    else:
        vehicle, created = Vehicle.objects.get_or_create(
            make=vehicle_data['make'],
            model=vehicle_data['model'],
            color=vehicle_data['color'],
            plate_number=vehicle_data['plate_number'])
    return vehicle, created
