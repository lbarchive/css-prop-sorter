all:
.PHONY: all

test:
	cd test && ./test.py
.PHONY: test

upload:
	python setup.py sdist --formats=bztar,gztar,zip bdist_wheel bdist_wininst --plat-name=win32 upload
