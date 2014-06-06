HERE = $(shell pwd)
BIN = $(HERE)/bin
PYTHON = $(BIN)/python

INSTALL = $(BIN)/pip install --no-deps
VTENV_OPTS ?= --distribute -p `which python2.7 python2.6 | head -n 1`

BUILD_DIRS = bin build include lib lib64 man share


.PHONY: all test docs build_extras

all: build

$(PYTHON):
	virtualenv $(VTENV_OPTS) .

build: $(PYTHON)
	$(PYTHON) setup.py develop

clean:
	rm -rf $(BUILD_DIRS)

test:
	$(BIN)/python setup.py test
