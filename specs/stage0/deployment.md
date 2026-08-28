# SDD Stage 1: Component Scaffolding

## Deployment Configuration

### 1. Docker Compose (`docker-compose.yml`)

- **Services**: Defines `api`, `frontend`, and `nginx` services.
- **Ports**: Exposes API on 8000, Frontend on 3000, Nginx on 80.
- **Volumes**:
  - `duckdb-data` named volume for persistent DuckDB database files (`/app/database`).
  - `./data:/app/data:ro` mounts the host's `data/` directory (containing `sample_data.csv`) as read-only into the API container.
- **Environment Variables**: `DATABASE_PATH` and `DATA_FILE` are set for the `api` service.

### 2. Nginx Configuration (`nginx/nginx.conf`)

- **Proxy Setup**: Configured as a reverse proxy inside the Docker network.
- **Routing**:
  - `/api/` path requests are forwarded to the `api` service (FastAPI).
  - All other requests (`/`) are forwarded to the `frontend` service (Next.js).
- **Headers**: Passes `Host`, `X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto` headers.

### 3. Service Dockerfiles

- **`backend/Dockerfile`**:
  - Base image: `python:3.12-slim`.
  - Installs dependencies from `requirements.txt`.
  - Copies application code.
  - Exposes port 8000.
  - Command: `uvicorn api.main:app --host 0.0.0.0 --port 8000`.
- **`frontend/Dockerfile`**:
  - Optimized for Next.js `standalone` output.
  - Uses a multi-stage build for a smaller final image.
  - Copies built application assets and serves on port 3000.

### 4. Deployment Notes

- **Containerization**: The entire application stack is containerized using Docker Compose.
- **Local Development**: `docker compose up -d` can be used to run the application locally.
- **External Access**: Service ports (80, 3000, 8000) are mapped from the host machine to the containers.
- **Host IP**: Deployment target `62.60.198.209` implies this setup is intended for a server environment.

### 5. Validation

- [x] Docker Compose file is syntactically correct.
- [x] Nginx configuration correctly proxies requests to backend and frontend.
- [x] Dockerfiles generate functional images for both services.
- [x] Volumes are correctly configured for data persistence and input.
