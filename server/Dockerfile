FROM python:3.8-slim-buster
COPY . .
RUN pip install flask
ENV FLASK_APP=server.py
EXPOSE 5000
CMD [ "flask", "run"]