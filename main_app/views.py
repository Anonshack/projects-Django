from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import Viloyat, Tuman, Stansiya, Osimlik, Hashorot, DataHashorot
from .serializers import ViloyatSerializer, TumanSerializer, StansiyaSerializer, OsimlikSerializer, HashorotSerializer, DataHashorotSerializer


class ViloyatViewSet(viewsets.ModelViewSet):
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer


class TumanViewSet(viewsets.ModelViewSet):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('tuman', )


class StansiyaViewSet(viewsets.ModelViewSet):
    queryset = Stansiya.objects.all()
    serializer_class = StansiyaSerializer


class OsimlikViewSet(viewsets.ModelViewSet):
    queryset = Osimlik.objects.all()
    serializer_class = OsimlikSerializer


class HashorotViewSet(viewsets.ModelViewSet):
    queryset = Hashorot.objects.all()
    serializer_class = HashorotSerializer


class DataHashorotViewSet(viewsets.ModelViewSet):
    queryset = DataHashorot.objects.all()
    serializer_class = DataHashorotSerializer