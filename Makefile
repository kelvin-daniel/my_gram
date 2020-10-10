runs:
	./manage.py runserver

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

