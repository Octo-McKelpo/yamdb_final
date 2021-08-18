FROM python:3.8.5
RUN workdir /code
COPY requirements.txt .
RUN pip3 install -r /code/requirements.txt
COPY . /code
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000 