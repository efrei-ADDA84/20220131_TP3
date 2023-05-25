FROM python:3.9
WORKDIR /app
COPY . /app
pip install -r requirements.txt
RUN
CMD ["uvicorn", "wrapper_api:app", "--host", "0.0.0.0", "--port", "8081"]
