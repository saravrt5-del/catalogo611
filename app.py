from flask import Flask, render_template
import csv

app = Flask(__name__)


def obtener_productos():
    productos = []

    with open("data/productos.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            productos.append(fila)

    return productos


@app.route("/")
def home():
    return render_template("pages/index.html")


@app.route("/productos")
def productos():

    productos = obtener_productos()

    return render_template(
        "pages/productos.html",
        productos=productos
    )


@app.route("/historia")
def historia():
    return render_template("pages/historia.html")


if __name__ == "__main__":
    app.run(debug=True)