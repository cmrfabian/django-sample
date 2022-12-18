## Compose sample application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/django)

### Django application in dev mode

Project structure:
```
.
├── docker-compose.yaml
├── Dockerfile
├── manage.py
├── README.md
├── requirements.txt
├── blog/
├── composeexample/
```

[_compose.yaml_](compose.yaml)
```
services:
  web:
    build: .
    command: >
      sh -c "python manage.py makemigrations &&
             python manage.py migrate &&
             python manage.py runserver 0.0.0.0:8000" 
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```

## Deploy with docker compose

```
$ docker compose up -d
Creating network "django_default" with the default driver
Building web
Step 1/6 : FROM python:3.7-alpine
...
...
Status: Downloaded newer image for python:3.7-alpine
Creating django_web_1 ... done

```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                    NAMES
85f61b608d5e   django-sample_web   "sh -c 'python manag…"   17 minutes ago   Up 17 minutes   0.0.0.0:8000->8000/tcp   django-sample-web-1
```

After the application starts, navigate to `http://localhost:8000` in your web browser:

Stop and remove the containers
```
$ docker compose down
```
