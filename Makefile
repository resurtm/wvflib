.PHONY: publish
publish:
	python setup.py sdist bdist_wheel upload

.PHONY: push
push:
	git push origin master && git push origin --tags
