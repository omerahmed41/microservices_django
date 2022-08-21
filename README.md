# microservice-django
A microservice blueprint built with python Django

Each service have their separate database completely decoupled. Nginx sits in front of each of the services to abstract all the microservices API endpoints into single one.
#### For first build:
* make setup
#### To run:
* make run
#### To stop:
* make stop


## Technology Stack & Features:
* Django fresh build
* RestFramework
* open API and swagger.
* docker with Docker compose.
* makefile.
* sample app
* Django signals.
* Logs.
* REDIS
* Celery
* Schedule Tasks (Django Q) 
* Custom exception handler
* message broker - rabbitmq.
* CI/CD Pipeline.
* kubernetes.
* Nginx API-gateway.
* Notification Service
* Design patterns (Pub-Sub, Command, Repository, Singleton).
* layer architecture (DDD).
* Frontend
* auth service- keycloak ( todo).
* Service registry.

# System Architecture:
![System Architecture](https://user-images.githubusercontent.com/15717941/185804170-07e3266b-a0c8-47b2-b0b7-c506731bb45d.jpg)



### to test the APIs see: 
#### http://127.0.0.1:8000/redoc/
#### http://127.0.0.1:8000/swagger/

## RabbitMq Dashboard:
* URL: http://localhost:15672
* username: guest
* password: guest
<img width="1440" alt="rabbitmq" src="https://user-images.githubusercontent.com/15717941/183268850-8a03311f-9409-4f19-ba30-10be962da86d.png">

## Docs:
#### I used OpenAPI with swagger for API docs, also  followed Domain driven design with services Layer architecture to make it easy to understand the code
#### Lastly the Naming of Classes, methods and objects is meaningful.

A Swager open API for djangorestframework to auto document your APIs

![Screen Shot 2022-07-04 at 2 21 23 PM](https://user-images.githubusercontent.com/15717941/177135399-ed503896-38f8-4fe0-a41f-1a769fe2d85f.png)

![Screen Shot 2022-07-04 at 2 21 55 PM](https://user-images.githubusercontent.com/15717941/177135458-10933058-acf7-4b25-85cc-8171654363a9.png)

## Communications: 
#### For Async communications I used rabbitmq, and for sync I used normal http calls later on grpc will be good use, also we can use REDIS as improvement.


## Design Patterns:
* Pub-Sub: I used bub-sub model along with events streaming broker rabbitmq.
* Repository: Used repository pattern to decouple Domain layer from DB layer, for example we can mock the repository and use DB memory.
* Singleton: Singleton pattern is used by  django for DBConnections.

## CI/CD:
#### Two steps: Build with tests, then Deploy.
#### I commented the part of pushing the images to DockerHub then uploading it to the cloud but, you can easily uncomment that to make it work.
<img width="1440" alt="Screen Shot 2022-08-21 at 6 37 42 PM" src="https://user-images.githubusercontent.com/15717941/185796382-343c44bb-7bbe-4ecc-9b89-49e727d37305.png">

## Todo:
#### the goal was to build the skeleton and base Architecture of the system, but these are Things need to be done when have more time: 
* Review and add more unit, integrations, contracts and acceptance tests.
* Build Frontend with React.js.
* Add more App Validations.
* Focus more on documentation.
* Auth Service with Keycloak.
* REDIS.
* GRPC (support HTTP2/Websocket).

* Note make sure you have Docker installed and give it enough memory from the setting, because we have 6 services running with 4 DBs.
<img width="1440" alt="Screen Shot 2022-08-07 at 3 53 13 PM" src="https://user-images.githubusercontent.com/15717941/183289201-10746be4-af21-4c2e-8242-bf1921c6faef.png">
