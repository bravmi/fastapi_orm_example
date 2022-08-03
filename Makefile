
run:
	uvicorn fastapi_orm_example.app:app --reload

get:
	http localhost:8000/users/?limit=100
