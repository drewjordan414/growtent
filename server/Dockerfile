# backend/Dockerfile
FROM python:3.8

WORKDIR /app

COPY server/requirements.txt ./
RUN pip install -r requirements.txt

COPY Server/ . 

CMD ["python", "app.py"]
