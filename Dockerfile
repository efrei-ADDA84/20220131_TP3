FROM python:3.9
WORKDIR /app
COPY . /app
run pip install requests
CMD ["uvicorn", "wrapper_api:app", "--host", "0.0.0.0", "--port", "8081"]
