from fastapi import FastAPI
import duckdb
import pathlib

app = FastAPI()

DB_PATH = pathlib.Path('/app/data/analytics.duckdb')

@app.on_event('startup')
async def load_db():
    if not DB_PATH.exists():
        # create simple schema and load sample CSV
        con = duckdb.connect(str(DB_PATH))
        con.execute("""
        CREATE TABLE sessions (
            merchant_key VARCHAR,
            session_status VARCHAR,
            amount BIGINT,
            adjusted_fee BIGINT,
            email VARCHAR,
            mobile VARCHAR,
            created_at TIMESTAMP
        );
        """)
        con.execute("COPY sessions FROM '/app/data/sample_data.csv' (HEADER, AUTO_DETECT TRUE);")
        con.close()

@app.get('/api/health')
async def health():
    return {"status": "healthy"}

@app.get('/api/analytics/overview')
async def overview():
    con = duckdb.connect(str(DB_PATH))
    res = con.execute('SELECT COUNT(*) AS total_sessions, SUM(amount) AS total_amount FROM sessions WHERE session_status = \'success\'').fetchone()
    con.close()
    return {"total_sessions": res[0], "total_amount": res[1]}
