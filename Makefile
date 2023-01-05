PIP_INSTALL_CMD=pip install \
	-r requirements.txt

install:
	${PIP_INSTALL_CMD}

service:
	python manage.py runserver