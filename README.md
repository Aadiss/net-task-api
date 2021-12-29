# net-task-api
This is my recruitment task API, which communicates  with an external API.

This simple API containts several endpoints which all are listed bellow. 

The overall point in here is to POST car make and model as a request body and after that my API shot to an external API which contains some informations about such make and model
for instance, if it exists.

You can also add or delete car to our database and rate them in scale 1-5.

---

API is available online via heroku. The url is: https://netg-api.herokuapp.com/

Anyway there is no endpoint like that so you can go directly to https://netg-api.herokuapp.com/cars

Deployment on Heroku was done according to this guide: https://testdriven.io/blog/deploying-django-to-heroku-with-docker/

If you use Apple M1 computer then this link might be helpful: https://stackoverflow.com/questions/66982720/keep-running-into-the-same-deployment-error-exec-format-error-when-pushing-nod

In case you want to use it locally you just need Docker installed, Dockerfile and docker-compose are prepared. App is connected with Postgres via docker-compose. Notice that you should change environment variables in docker-compose file. Each '*' sign should be changed.

---

There is a bunch of tests written, you can run all of them simply using this command:
> python manage.py test

To test it out you need to have installed dependencies included in requirements.txt file. Use virtualenv and run:

> pip install -r requirements.txt

---

## Documentation 

If any problem occurs with Postman or other testing tool / way, add to request headers:

Key: Content-Type

Value: application/json

## endpoint: 
>/cars

allowed methods: 
>POST, GET

**POST**

Request body pattern:

```json
 {
     "make" : "volkswagen",
     "model" : "golf",
}
```

In this endpoint user sends make and model, and then app checks if in external API such make and model exists. If yes then car is being saved in our databse.
If not, error response is returned with details. Comunication with external API is designed with 'requests' library. This is popular and simple Python library to sending requests and testing / comunicating with API's. 

**GET**
 
No request body, just returns all cars stored in database with id and average rate.

Example response:

>[
>
>    {
>    
>        "id": 1,
>        
>        "make": "volkswagen",
>        
>        "model": "passat",
>        
>        "avg_rating": 3.6
>        
>    },
>    
>    {
>    
>        "id": 2,
>        
>        "make": "volkswagen",
>        
>        "model": "golf",
>        
>        "avg_rating": null
>        
>    }
>    
>]

## endpoint: 
>/cars/{id}

allowed methods: 
>DELETE

This endpoint may delete car with provided id, if such car exists in our database. If car_id is invalid then an error occurs.

## endpoint: 
>/rate

allowed methods: 
>POST

Request body pattern:
> {
>
>     "car_id" : 1,
>
>     "rating" : 5,
>
>}

If you want to rate any car just send above request, if car_id is valid and rating value in range 1-5 then your rate will be created. 


## endpoint: 
>/popular

allowed methods: 
>GET

**GET**
 
No request body, just returns all cars stored in database with id and rates number, sorted by rates_number descending.

Example response:

>[
>
>    {
>    
>        "id": 1,
>        
>        "make": "volkswagen",
>        
>        "model": "passat",
>        
>        "rates_number": 2
>        
>    },
>    
>    {
>    
>        "id": 2,
>        
>        "make": "volkswagen",
>        
>        "model": "golf",
>        
>        "rates_number": 0
>        
>    }
>    
>]

# WARNING!

Before testing or trying to send request to HEROKU URL, pleasy visit above link first in order to 'awake' Heroku. 

