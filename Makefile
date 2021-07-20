SHELL := /bin/bash

include .env

.PHONY: help
help: ## Show this help
    @egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
    python3 -m venv $(VENV) && source $(BIN)/activate

.PHONY: install
install: venv ## Make venv and install requirements
    $(BIN)/pip install -r requirements.txt

migrate: ## Make and run migrations
    $(PYTHON) manage.py makemigrations test_auth_service_API
    $(PYTHON) manage.py migrate

.PHONY: test
test: ## Run tests
    $(PYTHON) $(APP_DIR)/manage.py test --verbosity=0 --parallel --failfast

.PHONY: run
run: ## Run the Django server
    $(PYTHON) $(APP_DIR)/manage.py runserver

start: install migrate run ## Install requirements, apply migrations, then start development server
