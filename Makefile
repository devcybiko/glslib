.PHONY: help install install-dev build clean test lint format

help:
	@echo "Available targets:"
	@echo "  install       - Install the package"
	@echo "  install-dev   - Install with development dependencies"
	@echo "  build         - Build distribution packages"
	@echo "  clean         - Remove build artifacts"
	@echo "  test          - Run unit tests"
	@echo "  lint          - Run linting checks"
	@echo "  format        - Format code with black"
	@echo "  all           - Clean, test, and build"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install pytest black flake8

build: clean
	pip install build
	python -m build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .eggs/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

test:
	python -m unittest discover tests/ -v

lint:
	flake8 glslib/ tests/ --max-line-length=100

format:
	black glslib/ tests/

all: clean test build
	@echo "✓ Build complete!"
