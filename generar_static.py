from app import app

paginas = [
    ("/", "index.html"),
    ("/productos", "productos.html"),
    ("/historia", "historia.html"),
]

with app.test_client() as client:
    for ruta, archivo in paginas:
        respuesta = client.get(ruta)
        contenido = respuesta.get_data(as_text=True)

        with open(f"dist/{archivo}", "w", encoding="utf-8") as f:
            f.write(contenido)

print("Listo: archivos creados en dist")