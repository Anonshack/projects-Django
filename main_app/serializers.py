from rest_framework import serializers
from .models import (
    Viloyat,
    Tuman,
    Stansiya,
    Osimlik,
    Hashorot,
    DataHashorot
)


class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = '__all__'


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = '__all__'


class StansiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stansiya
        fields = '__all__'


class OsimlikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osimlik
        fields = '__all__'


class HashorotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashorot
        fields = '__all__'


class DataHashorotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataHashorot
        fields = '__all__'
