#!/bin/bash

rm -f scenarios.tmp

for i in $(find behave -type f -name "*.feature");
do
    cat $i | grep "Scenario: " | sed 's/  Scenario: //' >> scenarios.tmp
done

#cat scenarios.tmp
while read p; do
  docker-compose exec -d worker python3 run_test.py "$p"
  echo $p
done <scenarios.tmp

todo=$(cat scenarios.tmp | wc -l | tr -d ' ')
done=$(docker-compose exec rabbit1 rabbitmqctl list_queues | grep behave | awk '{print $2}')

rm -f scenarios.tmp

sleep 5
while true
do
    left=$(docker-compose exec rabbit1 rabbitmqctl list_queues | grep behave | awk '{print $2}' | cat -v | sed -e 's/\^M//')
    if [ "$left" == "0" ]; then
      echo "Done"
      break

    fi
    echo "Todo: $todo, Left: $left"
done
