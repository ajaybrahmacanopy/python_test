# 🔄 CI/CD Guide - GitHub Actions

This project uses GitHub Actions for continuous integration and deployment.

## 📋 Workflows

### 1. **Run Tests** (`test.yml`)
Runs on: Every push and pull request to `main` or `develop`

**What it does:**
- ✅ Tests on Python 3.11 and 3.12
- ✅ Installs dependencies
- ✅ Runs flake8 linting
- ✅ Checks code formatting with black
- ✅ Runs pytest with coverage
- ✅ Uploads coverage to Codecov

**Badge:** 
```markdown
![Tests](https://github.com/ajaybrahmacanopy/python_test/workflows/Run%20Tests/badge.svg)
```

---

### 2. **Docker Build Test** (`docker-build.yml`)
Runs on: Every push and pull request to `main` or `develop`

**What it does:**
- 🐳 Builds Docker image
- 🧪 Tests the image by running a container
- ✅ Verifies health endpoint works
- ✅ Checks container logs
- 📊 Reports image size

**Badge:**
```markdown
![Docker Build](https://github.com/ajaybrahmacanopy/python_test/workflows/Docker%20Build%20Test/badge.svg)
```

---

### 3. **Deploy to Railway** (`deploy-railway.yml`)
Runs on: Push to `main` branch

**What it does:**
- ✅ Runs tests before deployment
- 🚀 Railway auto-deploys if tests pass
- 📝 Logs deployment status

**Badge:**
```markdown
![Deploy](https://github.com/ajaybrahmacanopy/python_test/workflows/Deploy%20to%20Railway/badge.svg)
```

---

### 4. **Code Quality** (`code-quality.yml`)
Runs on: Every push and pull request to `main` or `develop`

**What it does:**
- 🎨 Checks code formatting (black)
- 🔍 Runs linting (flake8)
- 🔎 Type checking (mypy)
- 🔒 Security scanning (bandit)
- 🛡️ Dependency vulnerability check (safety)

**Badge:**
```markdown
![Code Quality](https://github.com/ajaybrahmacanopy/python_test/workflows/Code%20Quality/badge.svg)
```

---

## 🚀 How It Works

### On Every Push/PR:
1. **Tests run automatically**
   - Unit tests
   - Integration tests
   - Code coverage

2. **Docker build test**
   - Ensures Docker image builds
   - Tests container functionality

3. **Code quality checks**
   - Formatting
   - Linting
   - Security

### On Push to Main:
1. All above checks run
2. If all pass → Railway auto-deploys
3. Your app goes live automatically! 🎉

---

## 📊 Viewing Results

### In GitHub:
1. Go to your repository
2. Click **"Actions"** tab
3. See all workflow runs
4. Click any run to see detailed logs

### Status Badges:
Add these to your README.md to show build status:

```markdown
![Tests](https://github.com/ajaybrahmacanopy/python_test/workflows/Run%20Tests/badge.svg)
![Docker Build](https://github.com/ajaybrahmacanopy/python_test/workflows/Docker%20Build%20Test/badge.svg)
![Deploy](https://github.com/ajaybrahmacanopy/python_test/workflows/Deploy%20to%20Railway/badge.svg)
```

---

## 🔧 Configuration

### Running Tests Locally

Before pushing, run tests locally:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/app --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_example.py

# Run tests in verbose mode
pytest -v
```

### Code Quality Checks

```bash
# Format code
black src/ tests/

# Check formatting without changing
black --check src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/
```

---

## 🛠️ Customizing Workflows

### Adding More Tests

Edit `.github/workflows/test.yml`:

```yaml
- name: Run integration tests
  run: |
    pytest tests/integration/ -v
```

### Changing Python Versions

Edit the matrix in `test.yml`:

```yaml
strategy:
  matrix:
    python-version: ['3.10', '3.11', '3.12']  # Add/remove versions
```

### Skip CI for Specific Commits

Add to commit message:
```bash
git commit -m "Update docs [skip ci]"
```

---

## 🔐 Secrets & Environment Variables

For sensitive data in CI:

1. Go to GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Add secrets like:
   - `RAILWAY_TOKEN` (if using Railway CLI)
   - `DATABASE_URL` (for testing)
   - `API_KEYS` (for external services)

Use in workflow:
```yaml
env:
  RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

---

## 📈 Coverage Reports

### Codecov Integration

1. Sign up at https://codecov.io with GitHub
2. Add repository
3. Coverage reports upload automatically
4. View coverage trends and reports

### Local Coverage

```bash
# Generate HTML coverage report
pytest --cov=src/app --cov-report=html

# Open report
open htmlcov/index.html
```

---

## 🐛 Troubleshooting CI

### Tests Pass Locally but Fail in CI

**Common causes:**
- Missing dependencies in `requirements.txt`
- Environment-specific issues
- Different Python versions

**Fix:**
```bash
# Test with same Python version as CI
pyenv install 3.11
pyenv local 3.11
pytest
```

### Docker Build Fails in CI

**Check:**
- Dockerfile syntax
- All files are committed
- .dockerignore isn't excluding needed files

**Debug:**
```bash
# Build locally
docker build -t test .

# Run locally
docker run -p 8000:8000 -e PORT=8000 test
```

### Workflow Not Triggering

**Check:**
- Workflow file syntax (YAML)
- Branch names match
- File is in `.github/workflows/`

---

## ✅ Best Practices

1. **Always run tests locally first**
   ```bash
   pytest && black src/ tests/ && flake8 src/ tests/
   ```

2. **Write tests for new features**
   - Add unit tests in `tests/unit/`
   - Add integration tests in `tests/integration/`

3. **Keep workflows fast**
   - Use caching
   - Run slow tests separately
   - Parallel execution

4. **Monitor CI status**
   - Fix failing tests quickly
   - Don't merge failing PRs

---

## 📚 Resources

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Docker CI Best Practices](https://docs.docker.com/build/ci/)
- [Railway CI/CD](https://docs.railway.app/deploy/deployments)

---

**Your CI/CD is now set up! Push your changes and watch the magic happen! ✨**

