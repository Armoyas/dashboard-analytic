# API Contract (Stage 1)

## Base URL & Endpoints

- Base URL: `http://localhost:8000/api`
- Endpoints: Detailed API endpoints for Merchants, Analytics, Sessions with filtering and pagination.

## Data Models & Schema

- Models: `Transaction`, `MerchantSummary`.
- Schema: DuckDB tables loaded from `data/sample_data.csv`.

## Validation

- API endpoints conform to schema.
- Data flow to frontend components validated.
