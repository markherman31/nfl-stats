check_install = python3 -c "import $(1)" || pip3 install $(1) --upgrade

lint:
	$(call check_install, black)
	black .

test: build
	python3 -m unittest discover -s test

build:
	poetry build

install:
	poetry install

.PHONY: all build test
