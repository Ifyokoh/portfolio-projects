FROM python:3.8
WORKDIR /code


RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
# COPY init-db.sql /docker-entrypoint-initdb.d/
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python", "app.py" ]