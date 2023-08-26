FROM python:3.8-alpine
WORKDIR /flaskProject

COPY . /flaskProject

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]