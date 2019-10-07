ARGUMENTS=$(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete
	-find . -type f -name "behave.log" -delete
	-rm -fr ./chrome_results/*
	-rm -fr ./firefox_results/*
	-rm -fr ./results/*

compile_requirements:
	@python3 -m piptools compile -U requirements.in

requirements:
	@pip install -r requirements.txt

containers:
	@docker-compose up --detach --build --scale worker=2

stop:
	@docker-compose rm --stop --force

test:
	@./run_tests.sh

scenarios:
	@PYTHONPATH=./ behave -d --no-summary --format mini features/ | sort

status:
	@redis-cli llen behave

results:
	./update_results.py firefox_results Firefox && \
	./update_results.py chrome_results Chrome && \
	rm -fr results/ && \
	mkdir results && \
	mv chrome_results/* results/ && \
	mv firefox_results/* results/ && \
	rm -fr chrome_results/ && \
	rm -fr firefox_results/

serve:
	@allure serve results/

report:
	@allure generate --clean --output ./report results/

pep8:
	@flake8 .

format:
	@isort --recursive .
	@black .

find_duplicated_scenario_names: SHELL:=/usr/bin/env bash  # set shell for this target to bash
find_duplicated_scenario_names:
	@diff -u <(PYTHONPATH=./ behave --dry --format mini --no-summary features/ | sort) \
		<(PYTHONPATH=./ behave --dry --format mini --no-summary features/ | sort -u)

.PHONY: build clean compile_requirements requirements containers stop test scenarios serve report results pep8 format find_duplicated_scenario_names
