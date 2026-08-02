import datetime
import platform

contenido = f"{datetime.datetime.now().isoformat()} {platform.node()} {platform.platform()}"

with open("spike-4.3/info.txt", "a", encoding="utf-8") as f:
    f.write(contenido + "\n")