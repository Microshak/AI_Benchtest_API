FROM python:3.8-buster
ADD . /code
WORKDIR /code
RUN pip install flask
RUN pip install redis
CMD ["python", "app.py"]
