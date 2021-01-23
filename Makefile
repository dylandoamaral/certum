test:
	@poetry run pytest --cov=certum --cov-config .coveragerc --cov-report=xml --cov-report=term tests/

clean:
	@poetry run black certum tests
	@poetry run isort certum tests

check:
	@poetry run pylint certum tests
	@poetry run black certum tests --check
	@poetry run isort certum tests --check