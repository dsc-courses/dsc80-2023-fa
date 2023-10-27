SHELL = /usr/bin/env bash

ASSIGNMENT_TYPE = discussion

# files used to determine if artifacts need to be rebuilt
BUILD_DEPENDENCIES = $(shell fd . src/ --no-ignore)


build/.sentinel: ${BUILD_DEPENDENCIES} src/ Makefile
	mkassignment build src/${ASSIGNMENT_TYPE}.ipynb build/
	touch build/.sentinel


.PHONY: check
check: build/.sentinel
	mkassignment check build/


.PHONY: clean
clean:
	rm -rf build
