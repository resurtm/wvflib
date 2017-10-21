PYTHON_CMD=/usr/bin/env python
COVERAGE_CMD=coverage

LIB_DIR=wvflib

TESTS_DIR=tests
TESTS_FILES='test_*.py'

COVERAGE_DIR=coverage
COVERAGE_HTML_DIR=coverage/html

SETUP_PY_FILE=setup.py

.PHONY: default tests publish push

default: tests

tests:
	$(COVERAGE_CMD) run --source=$(LIB_DIR) -m unittest discover -s $(TESTS_DIR) -p $(TESTS_FILES)

	mkdir -p $(COVERAGE_DIR)
	mkdir -p $(COVERAGE_HTML_DIR)

	$(COVERAGE_CMD) report -m
	$(COVERAGE_CMD) report -m > $(COVERAGE_DIR)/coverage.txt
	$(COVERAGE_CMD) html --directory=$(COVERAGE_HTML_DIR)

publish:
	$(PYTHON_CMD) $(SETUP_PY_FILE) sdist bdist_wheel upload

push:
	git push origin master && git push origin --tags
