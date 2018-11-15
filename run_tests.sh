#!/usr/bin/env bash

docker-compose exec worker sh -c "behave --dry-run -f mini --no-summary --tags=-wip behave/features/django_admin/" | while read -r line ; do
  docker-compose exec -d worker python3 run_test.py "chrome" "${line}"
  docker-compose exec -d worker python3 run_test.py "firefox" "${line}"
  echo $line
done
