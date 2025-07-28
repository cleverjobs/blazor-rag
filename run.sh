#!/bin/bash

set -e  # Exit on any error

echo "🚀 Starting RAG Scaffold Stage Environment..."

# === GIT SUBMODULES SECTION ===
echo "📦 Handling git submodules..."
git submodule update --init --recursive

if [ -f ".gitmodules" ]; then
  # Verify submodule directories exist and have content
  while IFS= read -r line; do
    if [[ $line =~ path[[:space:]]*=[[:space:]]*(.+) ]]; then
      submodule_path="${BASH_REMATCH[1]}"
      if [ ! -d "$submodule_path" ] || [ -z "$(ls -A "$submodule_path")" ]; then
        echo "❌ Error: Git submodule '$submodule_path' is not initialized or empty!" >&2
        echo "   This should not happen after 'git submodule update --init --recursive'" >&2
        exit 1
      fi
    fi
  done < .gitmodules
  echo "✅ Git submodules verified"
else
  echo "⚠️  No .gitmodules file found - skipping submodule check"
fi

# === GIT LFS SECTION ===
echo "📁 Handling Git LFS files..."
git lfs pull

# Verify LFS snapshot files
if [ ! -d "data/snapshots" ]; then
  echo "❌ Error: data/snapshots directory not found!" >&2
  echo "   Make sure you're running this from the project root directory." >&2
  exit 1
fi

if ! ls data/snapshots/*.snapshot 1> /dev/null 2>&1; then
  echo "❌ Error: No snapshot files found in data/snapshots/" >&2
  exit 1
fi

# Check if snapshot files have content (not just LFS pointers)
for snapshot in data/snapshots/*.snapshot; do
  if [ ! -s "$snapshot" ]; then
    echo "❌ Error: Snapshot file $snapshot is empty!" >&2
    echo "   This should not happen after 'git lfs pull'" >&2
    exit 1
  fi
  
  # Check if it's just a Git LFS pointer file
  if head -n 1 "$snapshot" | grep -q "version https://git-lfs.github.com/spec"; then
    echo "❌ Error: $snapshot is still a Git LFS pointer file!" >&2
    echo "   This should not happen after 'git lfs pull'" >&2
    exit 1
  fi
done

echo "✅ Git LFS snapshot files verified"

# === DOCKER SECTION ===
# Check if Docker is running
echo "🐳 Checking Docker..."
if ! docker info >/dev/null 2>&1; then
  echo "❌ Error: Docker is not running or not accessible!" >&2
  echo "   Please start Docker Desktop or Docker daemon." >&2
  exit 1
fi

echo "✅ Docker is running"

# Use docker compose if available, fallback to docker-compose
if docker compose version >/dev/null 2>&1; then
  docker compose -f docker-compose.stage.yml up --build
else
  docker-compose -f docker-compose.stage.yml up --build
fi