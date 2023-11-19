.PHONY: build
build:
	cd src && python build.py > ../build/index.html


watch:
	when-changed -r templates/ data/ src/ -1s -c make build

serve:
	cd build && python -m http.server 9090

deps/init:
	pip install pip-tools

deps/compile:
	pip-compile

deps/install: deps/init
	pip-sync
