FROM python:3

WORKDIR /opt/testing

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "worker", "-A", "tasks", "--loglevel=info", "-Q", "behave"]
