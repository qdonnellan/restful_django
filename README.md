# restful-django

This is just a dummy app to demonstrate how django-rest-framework can be implemented.

Download then install (you probably want to do this in virtualenv):

    pip install -r requirements.txt
   
Run the server

    ./manage.py runserver

Add an admin account so you can access the admin page

	./manage.py createsuperuser
	
View the admin portal at `/admin`

There is a dummy home page at `/` which is not handled by the API

There is only one model in the database: `Thing`

You can access the api for this model at `/api/things` - fun to play around with gets, posts, and puts