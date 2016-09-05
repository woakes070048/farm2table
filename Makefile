UNAME := $(shell uname)

.PHONY: test
test:
	py.test -s

.PHONY: run
run:
ifeq ($(UNAME), Darwin)
	python3 manage.py runserver
else
	python manage.py runserver
endif