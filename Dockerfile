FROM python:3.7.1

WORKDIR /opt/testing

RUN groupadd -r celery --gid 1000 && useradd --no-log-init -r -g celery --uid 1000 celery

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "worker", "--uid", "celery", "--app", "tasks", "--loglevel", "debug", "--queues", "behave", "--concurrency", "1"]
