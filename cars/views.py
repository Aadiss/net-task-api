from re import I
from requests import api
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError
from rest_framework.permissions import AllowAny

import requests

from .models import Car, Rating
from .serializers import CarOverallSerializer, RatingOverallSerializer, CarRatingSerializer


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def handle_cars(request):
    if request.method == 'GET':
        cars = Car.objects.all()

        serializer = CarRatingSerializer(cars, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        make = request.data.get('make')
        model = request.data.get('model')

        response = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json')
        response_json = response.json()

        if response.status_code != 200:
            raise NotFound(detail="Some error ocurred!", code=response.status_code)

        if response_json.get('Count') == 0:
            raise NotFound(detail="Error 404, No make found!", code=404)

        for result in response_json.get('Results'):
            if result.get('Model_Name').upper() == model.upper():

                try:
                    car = Car.objects.create(Make_Name=make, Model_Name=model)
                    serializer = CarOverallSerializer(car)

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except IntegrityError as e:
                    return Response({"error": f"{str(e)}, such make and model already exists in our database"}, status=status.HTTP_409_CONFLICT)

        raise NotFound(detail="Error 404, No model found!", code=404)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_by_id(request, id):
    try:
        car = Car.objects.get(pk=id)
        car.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_rate_by_id(request):
    car_id = request.data.get('car_id')
    rating = request.data.get('rating')
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise NotFound(detail="Such Car does not exist!", code=404)

    if 0 < int(rating) < 6:
        new_rating = Rating.objects.create(Car=car, Rate_Value=rating)

        serializer = RatingOverallSerializer(new_rating)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({"error": "Invalid rating value, 1-5 required"}, status=status.HTTP_400_BAD_REQUEST)

