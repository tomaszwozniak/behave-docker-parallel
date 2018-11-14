FROM python:3.7.1

WORKDIR /opt/testing

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "worker", "-A", "tasks", "--loglevel=info", "-Q", "behave", "-c", "1"]
