To start the project 
```shell
git clone https://github.com/GolamMullick/Bongo_project.git
cd core
docker-compose build
docker-compose up
```

To get the api collection

https://documenter.getpostman.com/view/8612995/UVC9gkFA

Every request need token 

To create admin token
```shell
docker-compose up -d
docker-compose exec web python manage.py createsuperuser
user_type should be admin
```
