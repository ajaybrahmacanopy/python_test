# 🚀 Quick Start: Deploy to Railway

## 🎯 What's Ready

Your FastAPI application is **100% configured** for Railway deployment with:

- ✅ Optimized Dockerfile with multi-stage build
- ✅ Railway configuration files (railway.toml, railway.json)
- ✅ Health check endpoint at `/health`
- ✅ Auto-reloading in development
- ✅ Production-ready settings

## 📦 Option 1: Deploy with Railway CLI (5 minutes)

### Step 1: Install Railway CLI

```bash
# macOS
curl -fsSL https://railway.app/install.sh | sh

# Or with Homebrew
brew install railway
```

### Step 2: Login to Railway

```bash
railway login
```

This will open your browser for authentication.

### Step 3: Deploy Your App

```bash
cd /Users/ajay.brahma/Documents/personal/python_deployment

# Initialize Railway project
railway init

# Deploy
railway up
```

### Step 4: Get Your Public URL

```bash
# Generate a public domain
railway domain

# Your app will be live at: https://python-deployment-production.up.railway.app
```

### Step 5: Test Your Deployment

```bash
# Replace with your actual Railway URL
curl https://your-app.up.railway.app/health
curl https://your-app.up.railway.app/docs
```

## 🌐 Option 2: Deploy with GitHub (Auto-Deploy on Push)

### Step 1: Push to GitHub

```bash
cd /Users/ajay.brahma/Documents/personal/python_deployment

# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit - FastAPI on Railway"

# Create a repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/python-deployment.git
git push -u origin main
```

### Step 2: Connect to Railway

1. Go to https://railway.app/new
2. Click **"Deploy from GitHub repo"**
3. Select your repository
4. Railway will **auto-detect** the Dockerfile and deploy

### Step 3: Configure Environment Variables (Optional)

In Railway Dashboard → Variables → Add:

```
APP_ENV=production
DEBUG=False
LOG_LEVEL=INFO
```

**Note:** Don't set `PORT` - Railway sets it automatically!

### Step 4: Generate Domain

1. Click **"Settings"** → **"Generate Domain"**
2. Your app is now live! 🎉

## 🧪 Testing Your Deployment

Once deployed, test all endpoints:

```bash
# Replace with your Railway URL
export APP_URL="https://your-app.up.railway.app"

# Health check
curl $APP_URL/health

# API documentation
open $APP_URL/docs

# Create an item
curl -X POST $APP_URL/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","description":"Testing on Railway","price":99.99}'

# Get all items
curl $APP_URL/api/v1/items
```

## 📊 Monitoring & Logs

### View Real-time Logs

```bash
# Using CLI
railway logs

# Or in Dashboard → Deployments → View Logs
```

### Check Deployment Status

```bash
railway status
```

### View Metrics

Go to Railway Dashboard → Your Project → Metrics to see:

- CPU usage
- Memory usage
- Request count
- Response times

## 🗄️ Adding a Database (Optional)

### Add PostgreSQL

```bash
# Using CLI
railway add postgresql

# Railway automatically sets DATABASE_URL
```

Then update your `requirements.txt`:

```
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
```

### Add Redis

```bash
# Using CLI
railway add redis

# Railway automatically sets REDIS_URL
```

Update `requirements.txt`:

```
redis>=5.0.0
```

## 🔄 Continuous Deployment

With GitHub connected:

```bash
# Make changes
vim src/app/api/example.py

# Commit and push
git add .
git commit -m "Add new feature"
git push

# Railway automatically deploys! 🚀
```

## 💰 Pricing

Railway charges based on usage:

- **Free Trial**: $5 credit
- **Developer Plan**: $5/month + usage
- Typical cost for this app: **$1-5/month**

## 🐳 Local Docker Testing (Optional)

Before deploying, test Docker locally:

```bash
# Start Docker Desktop first

# Build image
docker build -t python-deployment .

# Run container
docker run -p 8000:8000 -e PORT=8000 python-deployment

# Test
curl http://localhost:8000/health
```

## 🔧 Troubleshooting

### Build Failed

Check Railway logs:

```bash
railway logs
```

Common fixes:

- Ensure all files are committed
- Check `requirements.txt` is complete
- Verify `src/` directory structure

### App Won't Start

1. Check environment variables in Railway Dashboard
2. Ensure `PORT` is NOT manually set
3. Verify health check: `/health` endpoint works

### 502 Bad Gateway

- Health check might be failing
- Check logs: `railway logs`
- Ensure app binds to `0.0.0.0` not `localhost`

## 📚 Next Steps

- [ ] Set up custom domain
- [ ] Add database (PostgreSQL)
- [ ] Configure Redis cache
- [ ] Set up monitoring alerts
- [ ] Add authentication
- [ ] Configure CORS for production

## 🆘 Get Help

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- FastAPI Docs: https://fastapi.tiangolo.com

---

**Ready to deploy?** Just run:

```bash
railway login
railway init
railway up
railway domain
```

Your FastAPI app will be live in minutes! 🚀
