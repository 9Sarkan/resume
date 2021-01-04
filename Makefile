startDjango:
	python source/manage.py collectstatic --no-input
	python source/manage.py migrate
ifeq ("$(DEBUG_MODE)","True")
	python source/manage.py runserver 0.0.0.0:8000
else
	cd source && gunicorn source.wsgi -b 0.0.0.0:8000 --log-level=debug --log-file=-
endif

settings:
	cp source/base/settings.sample.py source/base/settings.py
