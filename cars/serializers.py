from rest_framework import serializers
from .models import Car, Rating


class CarOverallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'make',
            'model'
        ]


class RatingOverallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'Car',
            'Rate_Value'
        ]


class CarRatingSerializer(serializers.ModelSerializer):
    avg_rating = serializers.ReadOnlyField()

    class Meta:
        model = Car
        fields = [
            'id',
            'make',
            'model',
            'avg_rating'
        ]


class CarRatesNumberSerializer(serializers.ModelSerializer):
    rates_number = serializers.ReadOnlyField()

    class Meta:
        model = Car
        fields = [
            'id',
            'make',
            'model',
            'rates_number'
        ]