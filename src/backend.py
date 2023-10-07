import sqlite3

def connect() : 
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (id INTEGER PRIMARY KEY, date text, study text, project text, github_repos text, roadmap text, notes text)")
    conn.commit()
    conn.close()

def insert(date, study, project, github_repos, roadmap, notes) :
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL, ?, ?, ?, ?, ?, ?)", (date, study, project, github_repos, roadmap, notes))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rowe = cur.fetchall()
    conn.commit()
    conn.close()
    return rowe

def delete(id):
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
def search(date="", study="", project="", github_repos="", roadmap="", notes=""):
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR study=? OR project=? OR github_repos=? OR roadmap=? OR notes=?", (date, study, project, github_repos, roadmap, notes))
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

connect()