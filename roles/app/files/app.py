from flask import Flask, jsonify
import psycopg2
import os
app = Flask(__name__)

DB_CONFIG = {
    "host":     "postgres-container",
    "port":     5432,
    "dbname":   "appdb",
    "user":     "appuser",
    "password": os.environ.get("DB_PASSWORD", "supersecret123")
}

def get_db():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/')
def home():
    return '''
    <h1> Deployed with Ansible!</h1>
    <p> This app was automatically deployed using Ansible + Docker </p>
    '''
@app.route('/users')
def users():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email, created_at FROM users;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([
            {"id": r[0], "name": r[1], "email": r[2], "created_at": str(r[3])}
            for r in rows
        ])
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"})
    
    except Exception as e:
        return jsonify({"status": "unhealthy", "database": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)