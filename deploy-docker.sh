#!/bin/bash
# ─────────────────────────────────────────────────────────────────
#  deploy-docker.sh  —  Codex legalist Docker Deployment Script
# ─────────────────────────────────────────────────────────────────
set -e

echo "=> Fetching latest changes from Git..."
git fetch --all
git reset --hard origin/main

echo "=> Building Docker image..."
docker build --no-cache -t codex-legalist .

echo "=> Stopping and removing old container (if exists)..."
docker rm -f legalist_app || true

echo "=> Starting new Docker container on port 8000..."
docker run -d --name legalist_app -p 8000:8000 --restart unless-stopped codex-legalist

echo ""
echo "✅ Deployment complete! The app is running on port 8000."
echo "   Run 'docker logs -f legalist_app' to view live logs."
