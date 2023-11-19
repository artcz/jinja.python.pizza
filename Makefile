
deps/init:
	pip install pip-tools

deps/compile:
	pip-compile

deps/install: deps/init
	pip-sync
