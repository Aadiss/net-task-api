import re
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Car, Rating


class TestExternalAPI(APITestCase):
    def test_add_db_created(self):
        data = {
            "make": "volkswagen",
            "model": "tiguan"
        }
        response = self.client.post('/cars/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_conflicts(self):
        new_car = Car.objects.create(make='volkswagen', model='tiguan')

        data = {
            "make": "volkswagen",
            "model": "tiguan"
        }
        response = self.client.post('/cars/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_add_db_404(self):
        data = {
            "make": "intel",
            "model": "core"
        }
        response = self.client.post('/cars/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_db_404_model(self):
        data = {
            "make": "volkswagen",
            "model": "focus"
        }
        response = self.client.post('/cars/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestDeleteCars(APITestCase):
    def test_delete_first(self):
        new_car = Car.objects.create(make='ford', model='focus')
        response = self.client.delete('/cars/1/', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid(self):
        response = self.client.delete('/cars/1/', format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestRatings(APITestCase):
    def test_post_rating_valid(self):
        new_car = Car.objects.create(make='ford', model='focus')

        data = {
            "car_id": 1,
            "rating": 4
        }
        response = self.client.post('/rate/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_rating_no_car(self):
        data = {
            "car_id": 1,
            "rating": 4
        }
        response = self.client.post('/rate/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_rating_invalid_rating_gt(self):
        new_car = Car.objects.create(make='ford', model='focus')

        data = {
            "car_id": 1,
            "rating": 7
        }
        response = self.client.post('/rate/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_post_rating_invalid_rating_gt(self):
        new_car = Car.objects.create(make='ford', model='focus')

        data = {
            "car_id": 1,
            "rating": -2
        }
        response = self.client.post('/rate/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestGetCarsAvg(APITestCase):
    def test_avg_value(self):
        new_car = Car.objects.create(make='ford', model='focus')
        rating_1 = Rating.objects.create(Car=new_car, Rate_Value=5)
        rating_2 = Rating.objects.create(Car=new_car, Rate_Value=1)

        response = self.client.get('/cars/')

        self.assertEqual(response.json()[0]['avg_rating'], 3.0)

    def test_avg_null(self):
        new_car = Car.objects.create(make='ford', model='focus')

        response = self.client.get('/cars/')
    
        self.assertEqual(response.json()[0]['avg_rating'], None)


class TestPopularRating(APITestCase):
    def test_popular_number(self):
        new_car = Car.objects.create(make='ford', model='focus')
        rating_1 = Rating.objects.create(Car=new_car, Rate_Value=5)
        rating_2 = Rating.objects.create(Car=new_car, Rate_Value=1)

        response = self.client.get('/popular/')

        self.assertEqual(response.json()[0]['rates_number'], 2)

    def test_popular_number_no_ratings(self):
        new_car = Car.objects.create(make='ford', model='focus')

        response = self.client.get('/popular/')

        self.assertEqual(response.json()[0]['rates_number'], 0)

    def test_popular_number_order(self):
        new_car = Car.objects.create(make='ford', model='focus')
        new_car_2 = Car.objects.create(make='volkswagen', model='golf')
        Rating.objects.create(Car=new_car, Rate_Value=5)
        Rating.objects.create(Car=new_car, Rate_Value=1)

        Rating.objects.create(Car=new_car_2, Rate_Value=5)
        Rating.objects.create(Car=new_car_2, Rate_Value=1)
        Rating.objects.create(Car=new_car_2, Rate_Value=5)
        Rating.objects.create(Car=new_car_2, Rate_Value=1)

        response = self.client.get('/popular/')

        self.assertEqual(response.json()[0]['id'], 2)
        self.assertGreater(response.json()[0]['rates_number'], response.json()[1]['rates_number'])