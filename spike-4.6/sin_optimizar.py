import datetime, platform
print(datetime.datetime.now().isoformat(), platform.node(), platform.platform())

import sqlite3

con = sqlite3.connect("../spike.db")
cur = con.cursor()

query_count = 0

# 1 query
cur.execute("SELECT id, cliente_id, total FROM pedido")
pedidos = cur.fetchall()
query_count += 1

for pedido in pedidos:
    cur.execute("SELECT nombre FROM cliente WHERE id = ?", (pedido[1],))
    cur.fetchone()
    query_count += 1
    print(1)

print("TOTAL_QUERIES =", query_count)

con.close()