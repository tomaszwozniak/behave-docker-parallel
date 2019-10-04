# behave-docker-parallel
------------------------

# TODO

* distribute tasks across all browsers (or provide instruction to do so)
* run tests as non-root user (atm. allure_result_folder is owned by root!)
* implement scenarios that actually run in a browser


# Update requirements.txt

* Add new dependency to `requirements.in`
* Then compile new `requirements.txt` with [pip-compile](https://pypi.org/project/pip-tools/)

```shell
pip-compile -U -o requirements.txt requirements.in
```


## Start Hub & Browsers

Start Selenium Hub and 1 Firefox, 1 Chrome & 2 workers (1 for each browser)
```shell
docker-compose up --build --scale worker=2
```

Alternatively you can spin up multiple workers and instances of FF and/or Chrome:
```shell
docker-compose up --build --scale firefox=3 --scale chrome=3 --scale worker=6
```


## Run tests

```shell
./run_tests.sh
```

## Management & Monitoring Consoles

Once all services are up & running you can access:

* Selenium Grid Console [http://localhost:4444/grid/console](http://localhost:4444/grid/console)
* RabbitMQ Management UI Access [http://localhost:15672/](http://localhost:15672/) Credentials are: rabbitmq/rabbitmq


## Tips

### Checking health status of Selenium Hub & Browsers

You can check the health status of selenium-hub or selected browser with:

```shell
docker inspect --format='{{json .State.Health.Status}}' selenium-hub
# or
docker inspect --format='{{json .State.Health.Status}}' #BROWSER_INSTANCE_ID
```

or you can use a "get'em all" one-liner that displays health statuses for all 
browser instances and selenium-hub in one go:
```
docker inspect --format '{{ .Name }} -> {{ .State.Health.Status }}' \
    $(docker ps -a --format "table {{.Names}}\t{{.ID}}" |\
    grep "chrome\|firefox\|hub" |\
    awk '{printf $NF" "}')
```

btw. you can always create a handy alias for that one-liner:
```shell
alias hh='docker inspect --format "{{ .Name }} -> {{ .State.Health.Status }}" $(docker ps -a --format "table {{.Names}}\t{{.ID}}" | grep "chrome\|firefox\|hub" | awk '"'"'{printf $NF" "}'"'"')'
```

### Serving allure report

* Install [allure](https://docs.qameta.io/allure/#_installing_a_commandline)
* or if you're e.g. on Fedora then install [NPM wrapper around allure-commandline](https://www.npmjs.com/package/allure-commandline)
    * `npm install -g allure-commandline --save-dev`
* Serve the report `allure serve -p 54321 allure_results`
* Go to: [http://127.0.0.53:54321/](http://127.0.0.53:54321/)


### List all scenarios using mini formatter

```shell
# assuming that you're in the repo dir:
PYTHONPATH=./ behave -d -f mini behave/features/ --no-summary
```

