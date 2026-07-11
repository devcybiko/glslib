.PHONY: help install install-dev build clean test lint format venv

VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/python -m pip

help:
	@echo "Available targets:"
	@echo "  venv          - Create virtual environment"
	@echo "  install       - Install the package"
	@echo "  install-dev   - Install with development dependencies"
	@echo "  build         - Build distribution packages"
	@echo "  clean         - Remove build artifacts"
	@echo "  test          - Run unit tests"
	@echo "  lint          - Run linting checks"
	@echo "  format        - Format code with black"
	@echo "  all           - Clean, test, and build"

venv:
	@if [ ! -d $(VENV_DIR) ]; then \
		python3 -m venv $(VENV_DIR); \
		$(PYTHON) -m pip install --upgrade pip; \
		echo "✓ Virtual environment created"; \
	else \
		echo "✓ Virtual environment already exists"; \
	fi

install: venv
	$(PIP) install -e .

install-dev: venv
	$(PIP) install -e .
	$(PIP) install pytest black flake8 build

build: clean install-dev
	$(PYTHON) -m build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .eggs/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

test: install
	$(PYTHON) -m unittest discover tests/ -v

lint: install-dev
	$(PIP) install flake8
	$(PYTHON) -m flake8 glslib/ tests/ --max-line-length=100 || true

format: install-dev
	$(PIP) install black
	$(PYTHON) -m black glslib/ tests/

all: clean test build
	@echo "✓ Build complete!"
