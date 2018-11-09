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

Start Selenium Hub and 1 Firefox & 1 Chrome
```shell
docker-compose up --build
```

Alternatively you can spin up multiple workers and instances of FF and/or Chrome:
```shell
docker-compose up --build --scale firefox=3 --scale chrome=3 --scale worker=6
```


## Run tests

```shell
./run_tests.sh
```

## TIPS

### Selenium Grid Console

Selenium Grid Console is available via [http://localhost:4444/grid/console](http://localhost:4444/grid/console)


### Serving allure report

* Install [allure](https://docs.qameta.io/allure/#_installing_a_commandline)
* or if you're e.g. on Fedora then install [NPM wrapper around allure-commandline](https://www.npmjs.com/package/allure-commandline)
    * `npm install -g allure-commandline --save-dev`
* Serve the report `allure serve -p 54321 allure_results`
* Go to: [http://127.0.0.53:54321/](http://127.0.0.53:54321/)


### RabbitMQ Management UI Access

Once RabbitMQ is running you can access Management UI via: [http://localhost:15672/](http://localhost:15672/)
Credentials are: rabbitmq/rabbitmq

