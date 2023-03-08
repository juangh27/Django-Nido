# Django-Nido

## Comandos:
### Crear contenedor
> docker build -t django-nginx -f Dockerfile .

### Correr contenedor 
> docker run -p 8000:80 --name django-nginx --rm django-nginx 




Run services in the background: docker-compose up -d

Run services in the foreground: docker-compose up --build

Inspect volume: docker volume ls and docker volume inspect <volume name>

Prune unused volumes: docker volume prune

View networks: docker network ls

Bring services down: docker-compose down

Open a bash session in a running container: docker exec -it <container ID> /bin/bash

Open a bash session in a running container: docker exec -it <container ID> /bin/sh

Username: admin
Email address: juan@gmail.com
Password: 1234Qwer