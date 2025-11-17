# Deployment Guide - Railway

This guide walks you through deploying your FastAPI application to Railway.

## Prerequisites

- Railway account (https://railway.app)
- Railway CLI (optional, but recommended)
- GitHub account (recommended for automatic deployments)

## Method 1: Deploy with Railway CLI (Recommended)

### 1. Install Railway CLI

```bash
# macOS/Linux
curl -fsSL https://railway.app/install.sh | sh

# Or with Homebrew
brew install railway
```

### 2. Login to Railway

```bash
railway login
```

### 3. Initialize Railway Project

```bash
# From your project directory
cd /Users/ajay.brahma/Documents/personal/python_deployment

# Initialize Railway project
railway init
```

### 4. Set Environment Variables

```bash
# Set production environment variables
railway variables set APP_NAME=python-deployment
railway variables set APP_ENV=production
railway variables set DEBUG=False
railway variables set LOG_LEVEL=INFO

# Railway automatically sets PORT, don't override it
```

### 5. Deploy

```bash
# Deploy your application
railway up

# Or link to GitHub and deploy automatically
railway link
```

### 6. Get Your Deployment URL

```bash
railway domain
```

## Method 2: Deploy with GitHub (Automatic Deployments)

### 1. Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit for Railway deployment"

# Create a new repository on GitHub and push
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Deploy on Railway Dashboard

1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will auto-detect the Dockerfile

### 3. Configure Environment Variables

In Railway Dashboard:

1. Go to your project
2. Click on "Variables" tab
3. Add the following variables:

```
APP_NAME=python-deployment
APP_ENV=production
DEBUG=False
LOG_LEVEL=INFO
```

**Note:** Railway automatically provides the `PORT` variable. Don't set it manually.

### 4. Enable Public Domain

1. In your Railway project, go to "Settings"
2. Click "Generate Domain" to get a public URL
3. Your API will be available at: `https://your-app.up.railway.app`

## Adding Database (Optional)

### PostgreSQL

```bash
# Using CLI
railway add postgresql

# Railway will automatically set DATABASE_URL
```

### Redis

```bash
# Using CLI
railway add redis

# Railway will automatically set REDIS_URL
```

Or add them through the Railway Dashboard:

1. Click "New" in your project
2. Select "Database" → "PostgreSQL" or "Redis"
3. Railway will automatically inject connection URLs

## Update Your Application for Database

If you add PostgreSQL, update `requirements.txt`:

```bash
# Add to requirements.txt
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
alembic>=1.12.0  # for migrations
```

## Monitoring Your Deployment

### View Logs

```bash
# Using CLI
railway logs

# Or view in Dashboard under "Deployments" → "View Logs"
```

### Health Check

Once deployed, check your application:

```bash
# Replace with your Railway domain
curl https://your-app.up.railway.app/health
curl https://your-app.up.railway.app/docs
```

## Automatic Deployments

Railway automatically deploys when you push to your connected GitHub repository:

```bash
git add .
git commit -m "Update application"
git push origin main
# Railway will automatically detect and deploy changes
```

## Custom Domain (Optional)

1. Go to your project settings
2. Click "Custom Domain"
3. Add your domain and follow DNS configuration instructions

## Rollback Deployment

If something goes wrong:

```bash
# Using CLI - view deployments
railway status

# Rollback to previous deployment
railway rollback
```

Or in Dashboard:

1. Go to "Deployments"
2. Click on a previous successful deployment
3. Click "Redeploy"

## Cost

Railway offers:

- **Free Trial**: $5 credit
- **Developer Plan**: $5/month + usage
- **Team Plan**: $20/month per seat + usage

Your FastAPI app should cost approximately $1-5/month depending on traffic.

## Troubleshooting

### App won't start

Check logs:

```bash
railway logs
```

Common issues:

- Missing environment variables
- Port binding issues (ensure you're using `$PORT` from Railway)
- Missing dependencies in `requirements.txt`

### Health check failing

Ensure `/health` endpoint is accessible:

```bash
railway run python -c "import requests; print(requests.get('http://localhost:8000/health').json())"
```

## Next Steps

- [ ] Set up monitoring with Railway metrics
- [ ] Configure custom domain
- [ ] Set up CI/CD with GitHub Actions (if needed)
- [ ] Add database and Redis if needed
- [ ] Configure production logging
- [ ] Set up backup strategy for data

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- GitHub Issues: Create an issue in your repository
