import sqlite3
def init_db(path="sentinelpay.db"):
    con = sqlite3.connect(path)
    con.execute('''CREATE TABLE IF NOT EXISTS alerts (
        alert_id TEXT PRIMARY KEY, transaction_id TEXT, created_at TEXT,
        risk_score INTEGER, risk_band TEXT, reason_codes TEXT, status TEXT)''')
    con.commit()
    con.close()
