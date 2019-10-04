#!/usr/bin/env bash

docker-compose exec worker sh -c "PYTHONPATH=. behave --dry-run --no-source --no-summary --no-snippets --tags=-wip --format=mini features/" | while IFS=$'\r' read -r line ; do
  docker-compose exec -d worker python3 add_task.py "chrome" "${line}"
  docker-compose exec -d worker python3 add_task.py "firefox" "${line}"
  echo "Added task for scenario: '${line}'"
done
