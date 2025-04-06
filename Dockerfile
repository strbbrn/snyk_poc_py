# FROM python:3.9-slim
FROM python:3.14-rc-alpine5.6.2-r1
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
