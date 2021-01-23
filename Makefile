test:
	@poetry run pytest --cov=certum --cov-config .coveragerc tests/ -sq

clean:
	@poetry run black certum tests
	@poetry run isort certum tests

check:
	@poetry run flake8 certum tests
	@poetry run black certum tests --check
	@poetry run isort certum tests --check