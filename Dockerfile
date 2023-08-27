FROM python:3.8-alpine
WORKDIR /flaskProject

COPY . /flaskProject

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["gunicorn", "app:app" , "--bind", "0.0.0.0:5000", "-k", "eventlet", "--workers", "2"]