SHELL := /usr/bin/env bash

.PHONY: validate install clean

validate:
	bash scripts/validate.sh

install:
	mkdir -p ~/.agents/skills
	ln -sfn $(PWD)/skills/* ~/.agents/skills/
	@echo "Installed $(shell ls -d skills/*/ | wc -l) skills to ~/.agents/skills/"

clean:
	bash scripts/clean.sh
