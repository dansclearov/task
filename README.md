### To start:
```
docker-compose up
# Inside the container
python manage.py migrate
```

### _Notes_:
- I used docker so there is no need for a virtual environment
- CRUD operations are inherited from ModelViewSet, the rest are implemented
- Postman file for convenient testing

### Other futures:
- Pagination