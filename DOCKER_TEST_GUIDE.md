# 🐳 Docker Testing Guide - Step by Step

This guide walks you through testing your FastAPI application with Docker locally before deploying to Railway.

## Prerequisites

- ✅ Docker Desktop installed
- ✅ Docker Desktop running (whale icon in menu bar)
- ✅ Terminal open

## Step-by-Step Testing Process

### Step 1: Verify Docker is Running

**Command:**

```bash
docker --version
docker ps
```

**Expected Output:**

```
Docker version 28.x.x, build xxxxx
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

**What This Does:** Confirms Docker is installed and the daemon is running.

---

### Step 2: Navigate to Project Directory

**Command:**

```bash
cd /Users/ajay.brahma/Documents/personal/python_deployment
```

**Expected Output:**

```
(Should return to prompt with no errors)
```

**What This Does:** Changes to your project root directory where the Dockerfile is located.

---

### Step 3: Build the Docker Image

**Command:**

```bash
docker build -t python-deployment:latest .
```

**Expected Output:**

```
[+] Building 45.2s (14/14) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 1.2kB
 => [internal] load .dockerignore
 => [builder 2/4] COPY requirements.txt .
 => [builder 3/4] RUN pip install --no-cache-dir --user -r requirements.txt
 => [stage-1 4/6] COPY src/ ./src/
 => [stage-1 5/6] COPY config/ ./config/
 => exporting to image
 => => naming to docker.io/library/python-deployment:latest
```

**What This Does:**

- Reads the Dockerfile
- Creates a multi-stage build
- Installs Python dependencies
- Copies application code
- Creates a Docker image named `python-deployment:latest`

**Build Time:** ~30-60 seconds (first time), ~5-10 seconds (subsequent builds with cache)

---

### Step 4: Verify Image Was Created

**Command:**

```bash
docker images | grep python-deployment
```

**Expected Output:**

```
python-deployment   latest    abc123def456   2 minutes ago   165MB
```

**What This Does:** Lists Docker images and filters for your application image.

---

### Step 5: Run the Container

**Command:**

```bash
docker run -d \
  -p 8000:8000 \
  -e PORT=8000 \
  --name fastapi-test \
  python-deployment:latest
```

**Expected Output:**

```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

(A long container ID hash)

**What This Does:**

- `-d`: Runs container in detached mode (background)
- `-p 8000:8000`: Maps port 8000 on host to port 8000 in container
- `-e PORT=8000`: Sets environment variable PORT
- `--name fastapi-test`: Names the container for easy reference
- Returns the container ID

---

### Step 6: Check Container Status

**Command:**

```bash
docker ps
```

**Expected Output:**

```
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                    NAMES
a1b2c3d4e5f6   python-deployment:latest    "uvicorn app.main:ap…"   10 seconds ago  Up 9 seconds   0.0.0.0:8000->8000/tcp   fastapi-test
```

**What This Does:** Shows all running containers. Your container should be listed with STATUS "Up".

---

### Step 7: View Container Logs

**Command:**

```bash
docker logs fastapi-test
```

**Expected Output:**

```
INFO:     Will watch for changes in these directories: ['/app/src']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-11-17 23:45:12.123 | INFO     | app.main:lifespan:24 - Starting python-deployment...
2025-11-17 23:45:12.123 | INFO     | app.main:lifespan:25 - Environment: development
2025-11-17 23:45:12.123 | INFO     | app.main:lifespan:26 - Debug mode: True
INFO:     Application startup complete.
```

**What This Does:** Shows the logs from your FastAPI application inside the container.

**✅ Success Indicators:**

- "Application startup complete" message
- No error messages
- Port 8000 is mentioned

---

### Step 8: Test Health Endpoint

**Command:**

```bash
curl http://localhost:8000/health | python3 -m json.tool
```

**Expected Output:**

```json
{
  "status": "healthy",
  "timestamp": "2025-11-17T23:45:15.123456"
}
```

**What This Does:** Makes an HTTP request to the health check endpoint.

**✅ Success:** Returns JSON with `"status": "healthy"`

---

### Step 9: Test Root Endpoint

**Command:**

```bash
curl http://localhost:8000/ | python3 -m json.tool
```

**Expected Output:**

```json
{
  "message": "Welcome to the API",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

**What This Does:** Tests the root endpoint of your API.

---

### Step 10: Test Readiness Endpoint

**Command:**

```bash
curl http://localhost:8000/ready | python3 -m json.tool
```

**Expected Output:**

```json
{
  "status": "ready",
  "timestamp": "2025-11-17T23:45:20.123456"
}
```

**What This Does:** Tests the readiness check endpoint.

---

### Step 11: Test CRUD API - Create Item

**Command:**

```bash
curl -X POST http://localhost:8000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Docker Test","description":"Testing from Docker","price":99.99}' | python3 -m json.tool
```

**Expected Output:**

```json
{
  "name": "Docker Test",
  "description": "Testing from Docker",
  "price": 99.99,
  "id": 1
}
```

**What This Does:** Creates a new item via POST request.

---

### Step 12: Test CRUD API - Get All Items

**Command:**

```bash
curl http://localhost:8000/api/v1/items | python3 -m json.tool
```

**Expected Output:**

```json
[
  {
    "name": "Docker Test",
    "description": "Testing from Docker",
    "price": 99.99,
    "id": 1
  }
]
```

**What This Does:** Retrieves all items from the API.

---

### Step 13: Test API Documentation

**Command:**

```bash
# Open in browser
open http://localhost:8000/docs

# Or test with curl
curl http://localhost:8000/docs
```

**Expected Output:**

- Browser opens showing interactive Swagger UI documentation
- You can see all endpoints documented
- You can test endpoints directly from the browser

**What This Does:** Opens the interactive API documentation.

---

### Step 14: Monitor Logs in Real-time (Optional)

**Command:**

```bash
docker logs -f fastapi-test
```

**Expected Output:**

```
INFO:     127.0.0.1:52345 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52346 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:52347 - "POST /api/v1/items HTTP/1.1" 201 Created
...
```

**What This Does:** Shows real-time logs. Press `Ctrl+C` to stop following.

---

### Step 15: Inspect Container Details (Optional)

**Command:**

```bash
docker inspect fastapi-test
```

**Expected Output:**

```json
[
    {
        "Id": "a1b2c3d4e5f6...",
        "Created": "2025-11-17T23:45:10.123456Z",
        "State": {
            "Status": "running",
            "Running": true,
            ...
        },
        "Config": {
            "Env": [
                "PORT=8000",
                ...
            ]
        }
    }
]
```

**What This Does:** Shows detailed container configuration and state.

---

### Step 16: Check Container Resource Usage (Optional)

**Command:**

```bash
docker stats fastapi-test --no-stream
```

**Expected Output:**

```
CONTAINER ID   NAME          CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O
a1b2c3d4e5f6   fastapi-test  0.50%     45.2MiB / 7.768GiB   0.57%     1.5kB / 850B    0B / 0B
```

**What This Does:** Shows CPU, memory, and network usage of the container.

---

### Step 17: Execute Commands Inside Container (Optional)

**Command:**

```bash
docker exec -it fastapi-test /bin/bash
```

**Expected Output:**

```
root@a1b2c3d4e5f6:/app#
```

**What This Does:** Opens an interactive shell inside the container.

**Useful Commands Inside Container:**

```bash
# List files
ls -la

# Check Python version
python --version

# View installed packages
pip list

# Exit container
exit
```

---

### Step 18: Stop the Container

**Command:**

```bash
docker stop fastapi-test
```

**Expected Output:**

```
fastapi-test
```

**What This Does:** Gracefully stops the running container.

---

### Step 19: Verify Container Stopped

**Command:**

```bash
docker ps -a | grep fastapi-test
```

**Expected Output:**

```
a1b2c3d4e5f6   python-deployment:latest   ...   Exited (0) 5 seconds ago   fastapi-test
```

**What This Does:** Shows the container status as "Exited".

---

### Step 20: Remove the Container

**Command:**

```bash
docker rm fastapi-test
```

**Expected Output:**

```
fastapi-test
```

**What This Does:** Removes the stopped container from your system.

---

### Step 21: Remove the Image (Optional)

**Command:**

```bash
docker rmi python-deployment:latest
```

**Expected Output:**

```
Untagged: python-deployment:latest
Deleted: sha256:abc123...
Deleted: sha256:def456...
```

**What This Does:** Removes the Docker image from your system.

---

## Quick Test Script

Save this as a script for quick testing:

```bash
#!/bin/bash
# docker-test.sh

echo "🐳 Docker Test Script for FastAPI Application"
echo "=============================================="

# Navigate to project
cd /Users/ajay.brahma/Documents/personal/python_deployment

# Build image
echo -e "\n📦 Building Docker image..."
docker build -t python-deployment:latest .

# Run container
echo -e "\n🚀 Starting container..."
docker run -d -p 8000:8000 -e PORT=8000 --name fastapi-test python-deployment:latest

# Wait for startup
echo -e "\n⏳ Waiting for application to start..."
sleep 5

# Check logs
echo -e "\n📋 Container logs:"
docker logs fastapi-test | tail -10

# Test endpoints
echo -e "\n✅ Testing health endpoint:"
curl -s http://localhost:8000/health | python3 -m json.tool

echo -e "\n✅ Testing root endpoint:"
curl -s http://localhost:8000/ | python3 -m json.tool

echo -e "\n✅ Testing readiness endpoint:"
curl -s http://localhost:8000/ready | python3 -m json.tool

echo -e "\n✅ Creating test item:"
curl -s -X POST http://localhost:8000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Docker Test","description":"Automated test","price":99.99}' | python3 -m json.tool

echo -e "\n✅ Getting all items:"
curl -s http://localhost:8000/api/v1/items | python3 -m json.tool

# Container stats
echo -e "\n📊 Container stats:"
docker stats fastapi-test --no-stream

# Open docs
echo -e "\n📚 Opening API documentation in browser..."
open http://localhost:8000/docs

echo -e "\n✨ All tests completed!"
echo -e "\n💡 To view logs: docker logs -f fastapi-test"
echo -e "💡 To stop: docker stop fastapi-test"
echo -e "💡 To remove: docker rm fastapi-test"
```

## Troubleshooting

### Issue: Port 8000 already in use

**Solution:**

```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9
```

### Issue: Container won't start

**Check logs:**

```bash
docker logs fastapi-test
```

**Common fixes:**

- Ensure Dockerfile is correct
- Check all files are copied
- Verify requirements.txt is complete

### Issue: Cannot connect to Docker daemon

**Solution:**

1. Open Docker Desktop
2. Wait for it to fully start (whale icon turns stable)
3. Retry commands

### Issue: Build fails

**Check:**

- Internet connection (for downloading packages)
- Dockerfile syntax
- requirements.txt exists and is valid

## Success Checklist

After completing all steps, verify:

- [ ] Docker image builds successfully
- [ ] Container starts without errors
- [ ] Health endpoint returns 200 OK
- [ ] API documentation is accessible
- [ ] CRUD operations work
- [ ] Logs show no errors
- [ ] Container uses reasonable resources

## Next Steps

Once Docker testing is successful:

1. ✅ Your app is ready for Railway deployment
2. Push to GitHub
3. Deploy to Railway
4. Railway will use the same Dockerfile

---

**Your Docker setup is complete when all endpoints respond correctly!** 🎉
