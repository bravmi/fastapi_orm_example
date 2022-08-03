
run:
	uvicorn fastapi_orm_example.app:app --reload

get:
	http localhost:8000/users/?limit=100

lint:
	make flake8
	make mypy

flake8:
	flake8 .

mypy:
	mypy .
