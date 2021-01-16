# Makefile
format:
	black .
	isort .

lint:
	env PYTHONPATH=. pytest --flake8 --pylint --mypy --ignore=./tests/

utest:
	env PYTHONPATH=. pytest ./tests/ -s --verbose

setup:
	pip install -r requirements.txt
	pre-commit install
