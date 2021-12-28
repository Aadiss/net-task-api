from rest_framework import serializers
from .models import Car, Rating


class CarOverallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'Make_Name',
            'Model_Name'
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
            'Make_Name',
            'Model_Name',
            'avg_rating'
        ]