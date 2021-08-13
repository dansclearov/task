### To start:
```
docker-compose up
# Execute the next commands inside the container
python manage.py migrate
# Create a user
python manage.py createsuperuser
```

Optional features done:
- JWT authentification
- Docker image

### _Notes_:
- I used docker so there is no need for a virtual environment
- CRUD operations are inherited from ModelViewSet, the rest are implemented
- Postman [file](./task.postman_collection.json) for convenient testing
- 

### Other futures:
- Pagination