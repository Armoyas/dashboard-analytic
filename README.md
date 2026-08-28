# SDD Stage 1: Component Scaffolding

> Reference Repository: Armoyas/analytical-dashboard
> New Repository: Armoyas/dashboard-analytic
> Stage: Stage 1

## 1. Overview

This stage scaffolds the core components of the dashboard application. It includes:
- Frontend components and pages using Next.js 15.1.3.
- Backend API structure with FastAPI, DuckDB connection, and initial routes.
- Docker Compose setup for local development and deployment.
- Basic Nginx configuration.
- Initial DuckDB schema definition and CSV data loading script.

## 2. Deliverables

- **Frontend**:
  - `frontend/package.json`, `next.config.js`, `tailwind.config.js`, `postcss.config.js`
  - `frontend/app/layout.tsx`, `frontend/app/page.tsx`
  - `frontend/app/dashboard/page.tsx` (dynamic route)
  - `frontend/components/MerchantSelector.tsx`
  - `frontend/components/AnalyticsChart.tsx`
  - `frontend/components/DataTable.tsx`
- **Backend**:
  - `backend/requirements.txt`
  - `backend/api/main.py` (FastAPI app setup)
  - `backend/api/routers/*` (merchants, analytics, sessions)
  - `backend/api/models/schemas.py` (Pydantic models)
  - `backend/api/database/connection.py` (DuckDB connection & CSV loading)
  - `backend/api/services/zarrinpal.py` (Data loading logic)
- **Infrastructure**:
  - `docker-compose.yml`
  - `nginx/nginx.conf`
  - `backend/Dockerfile`, `frontend/Dockerfile`
  - `.env`, `.env.example`
  - `.gitignore`
- **Specs**:
  - `specs/stage1/README.md`
  - `specs/stage1/api-specs.md`
  - `specs/stage1/components.md`
  - `specs/stage1/database.md`
  - `specs/stage1/deployment.md`
  - `specs/stage1/testing.md`
  - `specs/stage1/validation.md`

## 3. Execution Steps

1.  **Clone Reference Repos**: `Armoyas/analytical-dashboard` and `Armoyas/dashboard` (implicitly done via copying specs).
2.  **Create `dashboard-analytic` repo**: Public repository created.
3.  **Copy Specs & Data**: Stage 0 and Stage 1 specs, along with `data/` folder, copied.
4.  **Install Speckit**: Via `lobe-skill-store` (assumed done).
5.  **Run Stage 0**: Project definition, architecture, requirements, API contract, validation.
6.  **Run Stage 1**: Scaffold frontend, backend, DuckDB schema, Docker Compose, Nginx config.
7.  **Commit & Push**: All changes pushed to `Armoyas/dashboard-analytic`.

## 4. Validation (Stage 1 - Manual & Automated)

- **Frontend**: Next.js 15.1.3 component imports, exports, and basic rendering verified. RTL support enabled.
- **Backend**: FastAPI application imports and basic router structure validated. DuckDB connection and CSV loading logic implemented.
- **Docker Compose**: Multi-container setup for API, Frontend, and Nginx confirmed. Volumes mounted for DuckDB and CSV data.
- **Nginx**: Basic reverse proxy configuration for API and Frontend paths.
- **Specs**: Stage 1 specification files created and available.

## 5. Notes

- **CSV Data**: Assumes `data/sample_data.csv` is present and correctly formatted.
- **DuckDB Schema**: `schema.sql` defines basic tables for merchants, sessions, and transactions.
- **Next.js Configuration**: `force-dynamic` and `standalone` output enabled.

## 6. Commit Message

`stage1: scaffold dashboard components and API structure`
