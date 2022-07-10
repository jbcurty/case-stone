FROM python:3.7.10-slim-stretch
WORKDIR /DEV
ADD . /DEV
#COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]
