from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("pages/index.html")

@app.route("/productos")
def productos():
    return render_template("pages/productos.html")

@app.route("/historia")
def historia():
    return render_template("pages/historia.html")

if __name__ == "__main__":
    app.run(debug=True)