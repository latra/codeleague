FROM python:3.6.10-alpine3.11

# Set environment variables.
# PYTHONDONTWRITEBYTECODE prevents Python from writing pyc files to disc.
# PYTHONUNBUFFERED Prevents Python from buffering stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app so any further instructions on the dockerfile
# occur within this directory.
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the image's filesystem at /app directory.
COPY requirements.txt /app/

# Install third dependencies for our dependency called psycopg2-binary.
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Install psql command used to check when postgres is ready.
RUN apk update && apk add postgresql-client

# Install chromium and chromium-chromedriver to E2E tests
RUN apk add chromium chromium-chromedriver

RUN pip install -r requirements.txt

COPY . /app
RUN adduser -D runner

USER runner