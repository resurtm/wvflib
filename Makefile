default: tests
.PHONY: tests
tests:
	coverage run --source=wvflib -m unittest discover -s tests -p test_*.py
	mkdir -p coverage/html
	coverage report -m
	coverage report -m > coverage/coverage.txt
	coverage html --directory=coverage/html

.PHONY: publish
publish:
	python setup.py sdist bdist_wheel upload

.PHONY: push
push:
	git push origin master && git push origin --tags
