# Stage 1 – Scaffold Specifications

The Scaffold stage defines the overall structure of the application and provides a concrete code base.

Key documents in this folder:

- `api-specs.md` – Detailed API endpoint specifications.
- `components.md` – Front‑end (Next.js 15) and back‑end (FastAPI) component architecture.
- `database.md` – DuckDB schema and sample queries.
- `deployment.md` – Docker‑Compose deployment workflow and Nginx configuration.
- `testing.md` – Unit, integration, and E2E testing outlines.
- `validation.md` – Validation checklist for the scaffold stage.

**Status:** Implemented in the `feature/stage1-scaffold` branch and merged via PR #1.

---

> **Note:** Stage 2 builds on this scaffold by adding `data/sample_data.csv`, initializing the DuckDB database, and providing minimal placeholder front‑end and back‑end implementations. Refer to `specs/stage2/` for the new implementation specifications.
