from django.shortcuts import render
from rest_framework import generics

from api.models import People
from api.serializers import PeopleSerializer
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
