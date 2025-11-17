.PHONY: help install install-dev run test lint format clean docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make run          - Run the FastAPI application"
	@echo "  make test         - Run tests with pytest"
	@echo "  make lint         - Run linters (flake8, mypy)"
	@echo "  make format       - Format code with black and isort"
	@echo "  make clean        - Remove cache and build files"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run   - Run with Docker Compose"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

run:
	python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest

test-cov:
	pytest --cov=src/app --cov-report=html --cov-report=term

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/
	isort src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete

docker-build:
	docker build -t python-deployment .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f

