FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /core
COPY requirements.txt /core/requirements.txt

RUN apt update -y
RUN apt install unixodbc-dev -y

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    odbcinst \
    odbcinst1debian2 \
    && rm -rf /var/lib/apt/lists/*

RUN echo "[ODBC Driver 17 for SQL Server]" >> /etc/odbcinst.ini
RUN echo "Description=Microsoft ODBC Driver 17 for SQL Server" >> /etc/odbcinst.ini
RUN echo "Driver=/usr/lib/odbc17.so" >> /etc/odbcinst.ini
RUN echo "UsageCount=1" >> /etc/odbcinst.ini


RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt
# RUN export LD_LIBRARY_PATH=`/opt/microsoft/msodbcsql17/lib64:$LD_LIBRARY_PATH`
RUN pip install -r requirements.txt
# RUN pip uninstall pyodbc
RUN pip install --no-binary :all: pyodbc

COPY . /core

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8004"]