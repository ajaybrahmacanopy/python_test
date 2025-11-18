# Python Application

![Lint](https://github.com/ajaybrahmacanopy/python_test/workflows/Lint%20Code/badge.svg)
![Tests](https://github.com/ajaybrahmacanopy/python_test/workflows/Run%20Tests/badge.svg)
![Docker Build](https://github.com/ajaybrahmacanopy/python_test/workflows/Docker%20Build%20Test/badge.svg)

## Project Overview

A well-structured FastAPI application with CI/CD, Docker support, and Railway deployment.

## Project Structure

```
python_deployment/
├── src/app/              # Main application code
│   ├── api/             # API endpoints/routes
│   ├── core/            # Core functionality
│   ├── models/          # Data models
│   ├── services/        # Business logic
│   └── utils/           # Utility functions
├── tests/               # Test suite
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
├── docs/               # Documentation
├── config/             # Configuration files
├── scripts/            # Utility scripts
├── logs/               # Application logs
└── data/               # Data files
    ├── raw/            # Raw data
    └── processed/      # Processed data
```

## Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

## Usage

### Running the Application

```bash
# Using uvicorn directly
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Or using make
make run

# Or using Python module
cd src && python -m app.main
```

### API Documentation

Once the application is running, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build and run manually
docker build -t python-deployment .
docker run -p 8000:8000 python-deployment
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/
```

## Development

### Code Style

This project follows PEP 8 guidelines. Use `black` for formatting and `flake8` for linting.

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/
```

## Deployment

### Railway Deployment

This application is configured for easy deployment on Railway.

#### Quick Deploy

1. Install Railway CLI:

```bash
curl -fsSL https://railway.app/install.sh | sh
```

2. Login and deploy:

```bash
railway login
railway init
railway up
```

3. Generate public domain:

```bash
railway domain
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

#### Deploy Button

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/yourusername/python-deployment)

## License

MIT License
