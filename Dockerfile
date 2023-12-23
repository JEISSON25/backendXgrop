FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /core
COPY requirements.txt /core/requirements.txt

RUN pip install --upgrade pip 
RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
RUN pip install -r requirements.txt

COPY . /core

# CMD ["python", "manage.py", "runserver 0:8000"]

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8004"]