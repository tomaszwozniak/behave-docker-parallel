# bin/bash

rm -f scenarios.tmp

for i in $(find behave -type f -name "*.feature");
do
    cat $i | grep "Scenario: " | sed 's/  Scenario: //' >> scenarios.tmp
    #echo $SCENARIO
    #python3 -c "from tasks import add; add.delay($)"
done

while read p; do
  python3 -c "from tasks import delegate_test; delegate_test.delay(\"$p\")"
done <scenarios.tmp

todo=$(cat scenarios.tmp | wc -l | tr -d ' ')
done=$(docker exec -ti behave-docker-parallel_rabbit1_1 rabbitmqctl list_queues | grep behave | awk '{print $2}')

rm -f scenarios.tmp

while true
do
    left=$(docker exec -ti behave-docker-parallel_rabbit1_1 rabbitmqctl list_queues | grep behave | awk '{print $2}')
#    if [ "$left" == "0" ]; then
#      break
#    fi
    echo $left
done
