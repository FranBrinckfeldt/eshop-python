FROM python:alpine
COPY [".", "/app"]
WORKDIR /app
RUN apk add --update musl-dev gcc libffi-dev
RUN pip install pipenv && pipenv sync
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV FLASK_ENV=development
CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]