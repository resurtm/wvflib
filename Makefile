PYTHON_CMD=/usr/bin/env python
COVERAGE_CMD=coverage

LIB_DIR=wvflib

TESTS_DIR=tests
TESTS_FILENAME='test_*.py'

COVERAGE_DIR=coverage
COVERAGE_HTML_DIR=coverage/html

.PHONY: default tests

default: tests

tests:
	date

	$(COVERAGE_CMD) run --source=$(LIB_DIR) -m unittest discover -s $(TESTS_DIR)

	mkdir -p $(COVERAGE_DIR)
	mkdir -p $(COVERAGE_HTML_DIR)

	$(COVERAGE_CMD) report -m
	$(COVERAGE_CMD) report -m > $(COVERAGE_DIR)/coverage.txt
	$(COVERAGE_CMD) html --directory=$(COVERAGE_HTML_DIR)

	date
