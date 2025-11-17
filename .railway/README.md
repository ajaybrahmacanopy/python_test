# Railway Deployment Configuration

This directory contains Railway-specific configuration files.

## Files

- `railway.toml` - Main Railway configuration
- `railway.json` - Alternative JSON configuration format
- `.env.railway` - Environment variables template for Railway

## Quick Deploy

```bash
# Install Railway CLI
curl -fsSL https://railway.app/install.sh | sh

# Login
railway login

# Deploy
railway up
```

## Environment Variables

Set these in Railway Dashboard or using CLI:

```bash
railway variables set APP_NAME=python-deployment
railway variables set APP_ENV=production
railway variables set DEBUG=False
railway variables set LOG_LEVEL=INFO
```

**Note:** Railway automatically provides `PORT` variable. Don't set it manually.

## Monitoring

View logs:

```bash
railway logs
```

View status:

```bash
railway status
```

## Domains

Generate a public domain:

```bash
railway domain
```

Or configure custom domain in Railway Dashboard.
