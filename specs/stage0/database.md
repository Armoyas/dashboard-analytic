# SDD Stage 1: Component Scaffolding

## Database Schema & Loading

### 1. Schema Definition (`database/schema.sql`)

- **`merchants` table**:
  - `merchant_key` (TEXT, PRIMARY KEY): Unique identifier for each merchant.
- **`sessions` table**:
  - `session_key` (TEXT, PRIMARY KEY): Unique ID for each payment session.
  - `merchant_key` (TEXT, NOT NULL, FOREIGN KEY references merchants): Link to the merchant.
  - `amount` (INTEGER, NOT NULL): Transaction amount in IRR.
  - `adjusted_fee` (INTEGER, NOT NULL): The adjusted fee.
  - `session_status` (TEXT, NOT NULL): Status of the session (e.g., 'completed', 'failed').
  - `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP): Timestamp of session creation.
- **`transactions` table**:
  - A direct copy of the `sessions` table content.

### 2. CSV Loading Mechanism (`backend/api/database/connection.py`)

- The `load_csv` function will parse the CSV file located at `DATA_FILE` (defaulting to `/app/data/sample_data.csv`).
- It intelligently creates or appends data to the `merchants` and `sessions` tables.
- DuckDB's `read_csv_auto` is used for schema inference.

### 3. Data Model (`backend/api/models/schemas.py`)

- **`Transaction` Pydantic Model**: Corresponds to the structure of rows in the `sessions` (and `transactions`) table.
- **`MerchantSummary` Pydantic Model**: Represents the aggregated summary data for a merchant.

### 4. Validation

- [x] Schema definition is valid SQL for DuckDB.
- [x] `load_csv` function correctly identifies and parses the CSV structure.
- [x] Primary and foreign key constraints are correctly defined.
- [x] Indexes are created on `merchant_key`, `session_status`, and `created_at` for query optimization.
