import sqlite3
from pathlib import Path

SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS dashers(id INTEGER PRIMARY KEY AUTOINCREMENT,display_name TEXT NOT NULL,headline TEXT NOT NULL DEFAULT 'Independent Delivery Professional',bio TEXT NOT NULL DEFAULT '',skills TEXT NOT NULL DEFAULT '',education TEXT NOT NULL DEFAULT '',career_interests TEXT NOT NULL DEFAULT '',public_profile INTEGER NOT NULL DEFAULT 1);
CREATE TABLE IF NOT EXISTS merchants(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,location_name TEXT NOT NULL,city TEXT NOT NULL,pilot_group TEXT NOT NULL DEFAULT 'general');
CREATE TABLE IF NOT EXISTS deliveries(id INTEGER PRIMARY KEY AUTOINCREMENT,external_order_ref TEXT NOT NULL UNIQUE,merchant_id INTEGER NOT NULL,dasher_id INTEGER NOT NULL,pickup_minutes REAL NOT NULL DEFAULT 0,completed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(merchant_id) REFERENCES merchants(id),FOREIGN KEY(dasher_id) REFERENCES dashers(id));
CREATE TABLE IF NOT EXISTS feedback(id INTEGER PRIMARY KEY AUTOINCREMENT,delivery_id INTEGER NOT NULL UNIQUE,well_presented INTEGER NOT NULL,insulated_bag INTEGER,respectful INTEGER NOT NULL,followed_instructions INTEGER NOT NULL,handled_carefully INTEGER NOT NULL,efficient_interaction INTEGER NOT NULL,recognition TEXT NOT NULL DEFAULT '',manager_note TEXT NOT NULL DEFAULT '',created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(delivery_id) REFERENCES deliveries(id));
"""

class Store:
    def __init__(self,path='instance/pro-network.sqlite3'):
        self.path=str(Path(path)); Path(self.path).parent.mkdir(parents=True,exist_ok=True); self.initialize()
    def connect(self):
        c=sqlite3.connect(self.path); c.row_factory=sqlite3.Row; c.execute('PRAGMA foreign_keys=ON'); return c
    def initialize(self):
        with self.connect() as c: c.executescript(SCHEMA)
    def dashers(self):
        with self.connect() as c: return [dict(r) for r in c.execute('SELECT * FROM dashers ORDER BY display_name')]
    def get_dasher(self,did):
        with self.connect() as c:
            r=c.execute('SELECT * FROM dashers WHERE id=?',(did,)).fetchone(); return dict(r) if r else None
    def unrated(self):
        with self.connect() as c:
            rows=c.execute('SELECT d.*,m.name merchant_name,m.location_name,da.display_name FROM deliveries d JOIN merchants m ON m.id=d.merchant_id JOIN dashers da ON da.id=d.dasher_id LEFT JOIN feedback f ON f.delivery_id=d.id WHERE f.id IS NULL ORDER BY d.id DESC').fetchall()
            return [dict(r) for r in rows]
    def submit_feedback(self,delivery_id,v):
        with self.connect() as c:
            c.execute('INSERT INTO feedback(delivery_id,well_presented,insulated_bag,respectful,followed_instructions,handled_carefully,efficient_interaction,recognition,manager_note) VALUES(?,?,?,?,?,?,?,?,?)',(delivery_id,v['well_presented'],v['insulated_bag'],v['respectful'],v['followed_instructions'],v['handled_carefully'],v['efficient_interaction'],v.get('recognition',''),v.get('manager_note','')))
    def metrics(self,did):
        with self.connect() as c: rows=[dict(r) for r in c.execute('SELECT f.* FROM feedback f JOIN deliveries d ON d.id=f.delivery_id WHERE d.dasher_id=?',(did,))]
        if not rows: return {'responses':0}
        def pct(k):
            vals=[r[k] for r in rows if r[k] is not None]
            return round(100*sum(vals)/len(vals),1) if vals else None
        return {'responses':len(rows),'professionalism':pct('well_presented'),'prepared':pct('insulated_bag'),'respectful':pct('respectful'),'order_care':pct('handled_carefully'),'efficient':pct('efficient_interaction')}
    def pilot_summary(self):
        with self.connect() as c:
            r=c.execute('SELECT COUNT(DISTINCT d.id) deliveries,COUNT(f.id) feedback_count,ROUND(AVG(d.pickup_minutes),2) avg_pickup_minutes,ROUND(100.0*AVG(f.respectful),1) respectful_pct,ROUND(100.0*AVG(f.well_presented),1) professional_pct FROM deliveries d LEFT JOIN feedback f ON f.delivery_id=d.id').fetchone()
            return dict(r)
