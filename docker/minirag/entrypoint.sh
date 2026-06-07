#!/bin/bash
set -e

echo "Starting Alembic migrations..."
cd /app/models/db_schemas/minirag/
alembic upgrade head
cd /app

exec "$@"
