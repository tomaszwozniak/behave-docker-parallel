#!/bin/bash

docker-compose exec worker behave -d -f mini behave/features/ --no-summary | while read -r line ; do
  docker-compose exec -d worker python3 run_test.py "$line"
  echo $line
done
