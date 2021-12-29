# net-task-api
This is my recruitment task API, which communicates  with an external API.

This simple API containts several endpoints which all are listed bellow. 

The overall point in here is to POST car make and model as a request body and after that my API shot to external API which contains some informations about such make and model
for instance, if it exists.

You can also add or delete car to our database and rate them in scale 1-5.

API is available online via heroku. The url is: https://netg-api.herokuapp.com/

Anyway there is no endpoint like that so you can go directly to https://netg-api.herokuapp.com/cars

Deployment on Heroku was done according to this guide: https://testdriven.io/blog/deploying-django-to-heroku-with-docker/

If you use Apple M1 computer then this link might be helpful: https://stackoverflow.com/questions/66982720/keep-running-into-the-same-deployment-error-exec-format-error-when-pushing-nod

In case you want to use it locally you just need Docker installed, Dockerfile and docker-compose are prepared. App is connected with Postgres via docker-compose. 

There is a bunch of tests written, you can run all of them simply using this command:
> python manage.py test

## Documentation 
endpoint: 
>/cars

allowed methods: 
>POST, GET

**POST**

Request body pattern:
> {
>
>     "make" : "volkswagen",
>
>     "model" : "golf",
>
>}

In this endpoint user sends make and model, and then app checks if in external API such make and model exists. If yes then car is being saved in our databse.
If not, error response is returned with details.

**GET**
 
No request body, just returns all cars stored in database with id and average rate.

Example response:
