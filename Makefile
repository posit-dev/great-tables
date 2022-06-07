.PHONY: check

test:
	pytest

check:
	pyright --pythonversion 3.7 gt
	pyright --pythonversion 3.11 gt

install: dist ## install the package to the active Python's site-packages
	python3 -m pip install --force-reinstall dist/gt*.whl