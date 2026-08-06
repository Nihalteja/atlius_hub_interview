import sqlite3
sql="""
CREATE TABLE organizations (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  active INTEGER NOT NULL  -- 1 active, 0 inactive
);
CREATE TABLE invoices (
  id INTEGER PRIMARY KEY,
  org_id INTEGER NOT NULL,
  amount INTEGER NOT NULL,          -- always > 0
  status TEXT NOT NULL,             -- 'draft' | 'paid' | 'void' | 'open'
  issued_on TEXT NOT NULL           -- 'YYYY-MM-DD'
);
CREATE TABLE payments (
  id INTEGER PRIMARY KEY,
  invoice_id INTEGER NOT NULL,
  amount INTEGER NOT NULL,          -- always > 0
  received_on TEXT NOT NULL
);
"""
sql="""
SELECT
    o.id,
    o.name,
    SUM(i.amount - COALESCE(p.total_paid, 0)) AS open_balance
FROM organizations o
JOIN invoices i
    ON o.id = i.org_id
LEFT JOIN (
    SELECT
        invoice_id,
        SUM(amount) AS total_paid
    FROM payments
    GROUP BY invoice_id
) p
ON i.id = p.invoice_id
WHERE o.active = 1
  AND i.status = 'open'
GROUP BY o.id, o.name
ORDER BY o.name;
"""

conn = sqlite3.connect("altius_hub.db")
cur = conn.cursor()
cur.executescript(sql)
conn.commit()
