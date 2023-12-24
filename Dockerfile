FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /core
COPY requirements.txt /core/requirements.txt

RUN apt update -y
RUN apt install unixodbc-dev -y
RUN pip install --upgrade pip 

# RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
# RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
RUN pip install --no-cache-dir -r requirements.txt
RUN export LD_LIBRARY_PATH=`/opt/microsoft/msodbcsql17/lib64:$LD_LIBRARY_PATH`
# RUN pip install -r requirements.txt
# RUN pip uninstall pyodbc
RUN pip install --no-binary :all: pyodbc
# RUN brew install unixodbc

COPY . /core

# CMD ["python", "manage.py", "runserver 0:8000"]

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8004"]