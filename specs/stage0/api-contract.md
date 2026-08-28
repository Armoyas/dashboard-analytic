# API Contract (Stage 1)

## Base URL & Endpoints

- Base URL: `http://localhost:8000/api`
- Endpoints: Merchants, Analytics, Sessions (all with filtering/pagination where applicable).

## Data Models & Schema

- Models: `Transaction`, `MerchantSummary`.
- Schema: DuckDB tables (`merchants`, `sessions`, `transactions`) loaded from `data/sample_data.csv`.

## Validation

- API endpoints conform to schema.
- Data flow to frontend is validated.
