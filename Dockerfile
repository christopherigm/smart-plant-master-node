FROM arm32v6/python:3.10.0rc2-alpine3.14

WORKDIR /app

COPY . .
COPY smart_plant/example.env smart_plant/.env

RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD [ "/bin/sh", "manage.py", "runserver", "0.0.0.0:8000" ]

