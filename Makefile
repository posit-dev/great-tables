.PHONY: check

test:
	pytest --cov=great_tables --cov-report=xml

test-no-pandas:
	pytest tests/test_dependencies.py -m "no_pandas"

test-update:
	pytest --snapshot-update

check:
	pyright --pythonversion 3.8 gt
	pyright --pythonversion 3.9 gt
	pyright --pythonversion 3.10 gt
	pyright --pythonversion 3.11 gt

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

dist: clean ## builds source and wheel package
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	ls -l dist

docs-build:
	cd docs \
	  && quartodoc build --verbose \
	  && quarto render

install: dist ## install the package to the active Python's site-packages
	python3 -m pip install --force-reinstall dist/gt*.whl

save-browser-table:
	python .github/scripts/save_browser_table.py _browser-tests.html chrome firefox

save-browser-table-ci:
	python .github/scripts/save_browser_table.py _browser-tests.html chrome firefox edge
