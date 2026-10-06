import os
import psycopg
from http.server import BaseHTTPRequestHandler, HTTPServer

DATABASE_URL = os.environ["DATABASE_URL"]

def registrar_visita():
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, fecha TIMESTAMP DEFAULT now())")
        conn.execute("INSERT INTO visitas DEFAULT VALUES")
        return conn.execute("SELECT count(*) FROM visitas").fetchone()[0]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.responder(200, "ok")
        elif self.path == "/visitas":
            total = registrar_visita()
            self.responder(200, f"Visitas registradas: {total}")
        else:
            self.responder(404, "no encontrado")

    def responder(self, codigo, texto):
        self.send_response(codigo)
        self.end_headers()
        self.wfile.write(texto.encode())

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()