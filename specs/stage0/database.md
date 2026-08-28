# SDD Stage 1: Component Scaffolding

> Reference Repository: Armoyas/analytical-dashboard
> New Repository: Armoyas/dashboard-analytic
> Stage: Stage 1

## 1. Data Model Definitions

### 1.1 `merchants` Table
- `merchant_key` (TEXT, PRIMARY KEY): Unique identifier for merchants.

### 1.2 `sessions` Table
- `session_key` (TEXT, PRIMARY KEY): Unique identifier for each payment session.
- `merchant_key` (TEXT, NOT NULL, FOREIGN KEY references merchants): The merchant associated with the session.
- `amount` (INTEGER, NOT NULL): Transaction amount in Iranian Rials (IRR).
- `adjusted_fee` (INTEGER, NOT NULL): The adjusted fee.
- `session_status` (TEXT, NOT NULL): Status of the session (e.g., 'completed', 'failed', 'pending').
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP): Timestamp of session creation.

### 1.3 `transactions` Table
- A direct copy of the `sessions` table for separate query access.

## 2. Database Operations

### 2.1 CSV Data Loading (`backend/api/database/connection.py`)
- The `load_csv` function will parse the CSV file located at `DATA_FILE` (defaulting to `/app/data/sample_data.csv`).
- It creates or appends to `merchants` and `sessions` tables.
- Schemas are inferred using `read_csv_auto`.

### 2.2 Schema Initialization (`database/schema.sql`)
- Defines `merchants`, `sessions`, and `transactions` tables.
- Includes indexes for `merchant_key`, `session_status`, and `created_at`.

## 3. API Integration

- **Merchants Router**: Endpoints to list merchants and retrieve merchant-specific summaries `/api/merchants`.
- **Analytics Router**: Endpoints for global dashboard overview `/api/analytics/overview` and transaction listing `/api/transactions`.
- **Sessions Router**: Endpoints for listing all sessions `/api/sessions` and retrieving specific session details.

## 4. Validation Criteria

- [x] Schema definition is valid SQL for DuckDB.
- [x] `load_csv` function correctly identifies and parses the CSV structure.
- [x] Primary and foreign key constraints are correctly defined.
- [x] Indexes are created for performance optimization.
