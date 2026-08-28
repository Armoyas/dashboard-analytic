# SDD Stage 1: Component Scaffolding

> Reference Repository: Armoyas/analytical-dashboard
> New Repository: Armoyas/dashboard-analytic
> Stage: Stage 1

## 1. Frontend Component Specifications

### 1.1 `MerchantSelector` (`frontend/components/MerchantSelector.tsx`)
- **Purpose**: Dropdown component to select a merchant for filtering.
- **Props**: `merchants` (array of strings), `selected` (current selection), `onChange` (callback function).
- **Functionality**: Renders a `<select>` element populated with merchant keys. Updates parent state via `onChange`.

### 1.2 `AnalyticsChart` (`frontend/components/AnalyticsChart.tsx`)
- **Purpose**: Displays a bar chart of session status counts.
- **Props**: `summary` (object containing `status_breakdown`).
- **Libraries**: Uses `react-chartjs-2` and `chart.js`.
- **Data Mapping**: Maps 'completed', 'failed', 'pending' statuses to chart segments.

### 1.3 `DataTable` (`frontend/components/DataTable.tsx`)
- **Purpose**: Renders transaction data in a tabular format.
- **Props**: `data` (array of transaction objects).
- **Columns**: Displays `session_key`, `merchant_key`, `amount`, `adjusted_fee`, `session_status`, `created_at`.
- **Styling**: Uses basic Tailwind CSS for table structure and readability.

## 2. Backend API Schema Definitions

### 2.1 Pydantic Models (`backend/api/models/schemas.py`)
- **`Transaction`**: Defines schema for individual transaction records.
- **`MerchantSummary`**: Defines schema for merchant summary data, including status breakdown.

### 2.2 API Route Responses
- **`GET /api/merchants`**: Returns `list[str]` (merchant keys).
- **`GET /api/merchants/{merchant_key}/summary`**: Returns `MerchantSummary` object.
- **`GET /api/analytics/overview`**: Returns `Dict[str, Any]` with global stats.
- **`GET /api/transactions`**: Returns `Dict[str, Any]` containing a list of `Transaction` objects and pagination info.
- **`GET /api/sessions`**: Returns `Dict[str, Any]` containing a list of sessions and pagination info.

## 3. Component Integration

- **`app/dashboard/page.tsx`**:
  - Fetches merchants in `useEffect`.
  - Fetches merchant summary and transactions based on `selectedMerchant`.
  - Renders `MerchantSelector`, `AnalyticsChart`, and `DataTable` by passing props.

## 4. Component-level Validation

- [x] All component imports are correct.
- [x] React hooks (`useState`, `useEffect`) used appropriately.
- [x] Props are passed correctly between parent and child components.
- [x] Basic error handling for API fetch failures (e.g., default values or empty states).
- [x] Chart.js and DataTable rendering data as expected from API responses.
