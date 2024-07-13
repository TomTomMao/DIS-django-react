from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.models import Ownership, People, Vehicle
from api.serializers import OwnershipSerializer, PeopleSerializer
from rest_framework.permissions import AllowAny
from django.db.models.functions import Concat
from django.db.models import Value, Q

# Create your views here.


class PeopleList(generics.ListAPIView):
    serializer_class = PeopleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        name = self.request.query_params.get('name')
        license = self.request.query_params.get('license')
        if name is None and license is None:
            queryset = People.objects.all()
        elif name is not None and license is not None:
            queryset = []
        elif license is not None:
            queryset = People.objects.filter(license__iexact=license)
        elif ' ' in name:
            queryset = People.objects.annotate(
                full_name=Concat('first_name', Value(' '), 'last_name')).filter(full_name__iexact=name)
        else:
            queryset = People.objects.all().filter(
                Q(first_name__iexact=name) | Q(last_name__iexact=name))
        return queryset

class OwnershipListCreate(generics.ListCreateAPIView):
    serializer_class = OwnershipSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        queryset = Ownership.objects.all()
        plate_number = self.request.query_params.get('plate_number', None)
        if plate_number:
            queryset = queryset.filter(vehicle__plate_number__iexact=plate_number)
        
        return queryset