.PHONY: check

test:
	pytest

check:
	pyright --pythonversion 3.7 gt
	pyright --pythonversion 3.11 gt