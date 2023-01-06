PIP_INSTALL_CMD=pip install \
	-r requirements.txt

install:
	${PIP_INSTALL_CMD}

load_db:
	python manage.py runscript load_db

clear_db:
	python manage.py runscript clear_db

service:
	python manage.py runserver