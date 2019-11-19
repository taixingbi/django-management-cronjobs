
### run pip shell
```
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### startproject and startapp
```
django-admin startproject mysite
python manage.py startapp polls
```

### run migrate
```
python manage.py makemigrations 
python manage.py migrate 
```


### run local
```
python manage.py runserver 0.0.0.0:8000
```





### run docker
```
docker-compose build
docker-compose up 
```

### run server
```
python manage.py runserver 0.0.0.0:8000 
```


http://localhost:8000/


### access container
```
docker exec -it containerId bash   
```

### more docker 
```
docker stop $(docker ps -aq)    
docker rm $(docker ps -aq)    
docker rmi $(docker images -q)
```


### reference
https://hub.docker.com/_/django/   
https://docs.docker.com/compose/django/





