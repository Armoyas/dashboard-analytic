# SDD Stage 1: Component Scaffolding

> Reference Repository: Armoyas/analytical-dashboard
> New Repository: Armoyas/dashboard-analytic
> Stage: Stage 1

## 1. Overview

This stage focuses on scaffolding the core components of the dashboard application, setting up the frontend, backend, and infrastructure based on Stage 0 definitions and the reference repository's patterns.

## 2. Frontend Scaffolding (`frontend/`)

### 2.1 Project Setup
- **Dependencies**: `next`, `react`, `react-dom`, `recharts`, `date-fns`.
- **Build**: Next.js 15.1.3 with `output: 'standalone'` and `force-dynamic`.
- **Styling**: Tailwind CSS v4 with PostCSS and Autoprefixer.
- **Configuration**: `next.config.js`, `tailwind.config.js`, `postcss.config.js`.

### 2.2 Application Structure (`app/`)
- **`layout.tsx`**: Main layout with RTL support (Persian `lang="fa"`), Inter font, and global CSS.
- **`page.tsx`**: Home page with branding and a link to the dashboard.
- **`dashboard/page.tsx`**: The main dashboard view, dynamically rendered, with merchant selection, summary chart, and data table.

### 2.3 Components (`components/`)
- **`MerchantSelector.tsx`**: Dropdown to filter data by merchant.
- **`AnalyticsChart.tsx`**: Bar chart displaying session status breakdown.
- **`DataTable.tsx`**: Table to display transaction data.

## 3. Backend Scaffolding (`backend/`)

### 3.1 Core Setup
- **Dependencies**: `fastapi`, `uvicorn`, `duckdb`, `pandas`, `pydantic`, `python-multipart`.
- **Main Application**: `api/main.py` sets up FastAPI, CORS middleware, and includes routers.
- **Health Check**: `/api/health` endpoint.

### 3.2 API Endpoints & Routers
- **Merchants**:
  - `GET /api/merchants`: Lists distinct merchant keys.
  - `GET /api/merchants/{merchant_key}/summary`: Provides summary stats for a merchant.
- **Analytics**:
  - `GET /api/analytics/overview`: Global dashboard statistics.
  - `GET /api/transactions`: Lists transactions with filtering/pagination.
- **Sessions**:
  - `GET /api/sessions`: Lists all payment sessions with pagination.
  - `GET /api/sessions/{session_key}`: Retrieves details for a specific session.

### 3.3 Data Handling
- **Models**: Pydantic models (`schemas.py`) for `Transaction` and `MerchantSummary`.
- **Database**: `connection.py` handles DuckDB connection and CSV loading logic.
- **Services**: `zarrinpal.py` ensures CSV data loading.

## 4. Infrastructure Setup

### 4.1 Docker Compose (`docker-compose.yml`)
- **Services**: `api`, `frontend`, `nginx`.
- **Ports**: API (8000), Frontend (3000), Nginx (80).
- **Volumes**: `duckdb-data` for persistence, `./data:/app/data:ro` for CSV input.

### 4.2 Nginx Configuration (`nginx/nginx.conf`)
- Reverse proxy setup to route `/api/*` to the API service and `/*` to the frontend.

### 4.3 Service Dockerfiles
- **`backend/Dockerfile`**: Optimized Python image with dependencies.
- **`frontend/Dockerfile`**: Optimized for Next.js standalone output.

### 4.4 Environment & Gitignore
- **`.env` / `.env.example`**: Configuration for database path and data file.
- **`.gitignore`**: Standard ignores for Node.js, Python, Docker, and OS files.

## 5. Specification Files (`specs/stage1/*`)

- `specs/stage1/README.md`
- `specs/stage1/api-specs.md`
- `specs/stage1/components.md`
- `specs/stage1/database.md`
- `specs/stage1/deployment.md`
- `specs/stage1/testing.md`
- `specs/stage1/validation.md`

## 6. Commit Message

`stage1: scaffold dashboard components and API structure`