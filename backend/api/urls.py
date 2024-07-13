from django.urls import path
from . import views

urlpatterns = [
    path("people/", views.PeopleList.as_view())
]
