# create user 
```
echo 'create User email="hdidiersharif@gmail.com" password="sheezy" fullname="habimanadidiersharif" cover="sharif" profilepicture="sharif" bio="holla"' | HBNB_MYSQL_USER=sheezy HBNB_MYSQL_PWD=sheezy HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=memedom HBNB_TYPE_STORAGE=db ./console.py 
```
# create Post
```
echo 'create Post owner="a62a7ab8-163d-4fff-9c97-020d270a3110" post="shanbreezy" ' | HBNB_MYSQL_USER=sheezy HBNB_MYSQL_PWD=sheezy HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=memedom HBNB_TYPE_STORAGE=db ./console.py 
```

# API
```
HBNB_MYSQL_USER=sheezy HBNB_MYSQL_PWD=sheezy HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=memedom HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
```

curl  -X POST http://127.0.0.1:5000/api/v1/users/signup -H "content-Type:application/json" -d '{email="hdidiersharif@gmail.com" password="sheezy" fullname="habimanadidiersharif" cover="sharif" profilepicture="sharif" bio="holla"}'
curl -