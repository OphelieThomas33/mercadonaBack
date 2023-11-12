
# MercadonaBack

Back End and API of the project to develop an online catalog as part of a certifying evaluation for the STUDI school.

This project is developed with the MercadonaFront project. These 2 projects are complementary to operate the Mercadona online catalog.


## Get started

### Prerequisites

To run the program, the `pip` dependency must be installed.

### Installation

#### Clone the repository

```shell
git clone https://github.com/OphelieThomas33/mercadonaBack.git
cd mercadonaBack
```

#### Install npm packages

```shell
  pip install -r requirements.txt
```


### Specify environment Variables

To run this project, you will need to add the following environment variables to `.env` file in `mercadonaBackEnd` folder.

```python
`SECRET_KEY` : secret key django
`DEBUG` : True (develop) or False (prod)
`ALLOWED_HOSTS` : hosts allowed to communicate with back
`CSRF_TRUSTED_ORIGINS` : url of your API
`SWAGGER_URL` : url of your API
`DB_NAME` : database name
`DB_USER` : database username
`DB_PASSWORD` : database password
`DB_HOST` : database host
`DB_PORT` : database port
```

### Generate databse tables

To import data model information into the database, copy these instructions in the shell :

```shell
python manage.py migrate
```


## Use

### Development server

Run `python manage.py runserver` for a dev server. Navigate to `http://localhost:8000/`. The application will automatically reload if you change any of the source files.

### Urls

#### Django admin panel

The django admin panel will allow the creation of users and the assignment of a group (USER or ADMIN).  
Here is the url to call the django panel admin : 
`http://yourhostname/admin`

#### API 

Here is the url to call the API : 
`http://yourhostname/api` 

#### Swagger 

Here is the url to call the swagger schema : 
`http://yourhostname/api/swagger/schema`

Here is the url to call the swagger redoc : 
`http://yourhostname/api/swagger/redoc`

## Deploy

### uwsgi

Create `mercadona_uwsgi.ini` in mercadonaBackEnd folder and define following variables :

```
chdir = /path/to/mercadonaBackEnd
module = mercadonaBackEnd.wsgi
http = 127.0.0.1:8000
master = true
vacuum = true
```

Launch the file `mercadona_uwsgi.ini` on your server with this instruction (if Nginx server) :
```shell
uwsgi --ini mercadona_uwsgi.ini
```

