runs:
	./manage.py runserver

check:
	./manage.py check

test:
	./manage.py test my_gram
	
superuser:
	./manage.py createsuperuser --username $(name)

collectstatic:
	./manage.py collectstatic

migrations:
	./manage.py makemigrations $(app)

migrate:
	./manage.py migrate

start:
	django-admin startapp $(name)

