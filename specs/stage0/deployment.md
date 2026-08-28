# SDD Stage 1: Component Scaffolding

## 1. Deployment Configuration

### 1.1 Docker Compose (`docker-compose.yml`)
- **Services**: `api`, `frontend`, `nginx`.
- **Ports**: API (8000), Frontend (3000), Nginx (80).
- **Volumes**: `duckdb-data` for persistence, `./data:/app/data:ro` for CSV input.
- **Environment Variables**: `DATABASE_PATH`, `DATA_FILE` set for the `api` service.

### 1.2 Nginx Configuration (`nginx/nginx.conf`)
- Reverse proxy setup for `/api/*` to API and `/*` to Frontend.

### 1.3 Service Dockerfiles
- **`backend/Dockerfile`**: Python 3.12 slim image, installs dependencies.
- **`frontend/Dockerfile`**: Optimized for Next.js standalone output.

### 1.4 Deployment Notes
- Containerized stack via Docker Compose.
- Local development via `docker compose up -d`.
- Host IP for deployment: `62.60.198.209`.

### 1.5 Validation
- [x] Docker Compose file is syntactically correct.
- [x] Nginx configuration correctly proxies requests.
- [x] Dockerfiles generate functional images.
- [x] Volumes are correctly configured.
