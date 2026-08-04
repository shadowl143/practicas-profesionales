# seed.py — 20 clientes, 200 pedidos. Solo stdlib.
import sqlite3, random

def seed(db="spike.db", n_clientes=20, n_pedidos=200, semilla=42):
    random.seed(semilla) # reproducible: mismo dataset para todos
    con = sqlite3.connect(db)
    con.executescript("""
    DROP TABLE IF EXISTS pedido; DROP TABLE IF EXISTS cliente;
    CREATE TABLE cliente (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL);
    CREATE TABLE pedido (id INTEGER PRIMARY KEY, cliente_id INTEGER NOT NULL,
    total REAL NOT NULL, FOREIGN KEY (cliente_id) REFERENCES cliente(id));
    """)
    con.executemany("INSERT INTO cliente (id, nombre) VALUES (?, ?)",
    [(i, f"Cliente {i:02d}") for i in range(1, n_clientes + 1)])
    con.executemany("INSERT INTO pedido (id, cliente_id, total) VALUES (?, ?, ?)",
    [(i, random.randint(1, n_clientes), round(random.uniform(50, 5000), 2))
    for i in range(1, n_pedidos + 1)])
    con.commit()
    print(f"seed listo: {n_clientes} clientes, {n_pedidos} pedidos en {db}")
    con.close()

if __name__ == "__main__":
    seed()