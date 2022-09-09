
run:
	uvicorn fastapi_orm_example.app:app --reload --use-colors

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
