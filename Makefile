
run:
	python app/manage.py

get:
	http localhost:8000/users/?limit=2

lint:
	make flake8
	make mypy

flake8:
	flake8 .

mypy:
	mypy .

update:
	poetry update -vv
