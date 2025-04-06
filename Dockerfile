FROM python:3.14-rc-alpine3.20
RUN apk update && apk add --no-cache xz>=5.6.2-r1
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
