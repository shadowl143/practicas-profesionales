import datetime, platform
print(datetime.datetime.now().isoformat(), platform.node(), platform.platform())

import sqlite3

con = sqlite3.connect("../spike.db")
cur = con.cursor()

query_count = 0

cur.execute("""
SELECT pedido.id, cliente.nombre, pedido.total
FROM pedido
JOIN cliente ON pedido.cliente_id = cliente.id
""")
cur.fetchall()
query_count += 1

print("TOTAL_QUERIES =", query_count)

con.close()