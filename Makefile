SHELL := /usr/bin/env bash

.PHONY: validate install clean changelog tag

validate:
	bash scripts/validate.sh

install:
	mkdir -p ~/.agents/skills
	ln -sfn $(PWD)/skills/* ~/.agents/skills/ 2>/dev/null || true
	@echo "Installed $$(ls -d skills/*/ | wc -l) skills to ~/.agents/skills/"

clean:
	bash scripts/clean.sh

changelog:
	@echo "=== Latest entry ==="
	@awk '/^## \[/{c++} c==1{print} c==2{exit}' CHANGELOG.md

tag:
	@if [ -z "$(V)" ]; then \
		echo "Usage: make tag V=v0.x.x"; exit 1; \
	fi
	@echo "Creating tag $(V)..."
	@git tag -a "$(V)" -m "Release $(V)"
	@echo "Tag $(V) created. Review with: git log --oneline $(V) --not --all"
	@echo "Push with: git push origin $(V)"
