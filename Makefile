UNAME := $(shell uname)

.PHONY: test
test:
	python3 manage.py test

.PHONY: run
run:
ifeq ($(UNAME), Darwin)
	python3 manage.py runserver
else
	python manage.py runserver
endif