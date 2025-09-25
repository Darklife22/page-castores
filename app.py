from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "castores-secret-key"

@app.route("/")
def home():
    return render_template("index.html", page="inicio")

@app.route("/menu")
def menu():
    # Placeholder page (to be implemented)
    return render_template("menu.html", page="menu")

@app.route("/sucursales")
def sucursales():
    # Placeholder page (to be implemented)
    return render_template("sucursales.html", page="sucursales")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        # Here you can hook up email or database logic
        flash("¡Gracias! Recibimos tu mensaje y te responderemos pronto.", "success")
        return redirect(url_for("contacto"))
    return render_template("contacto.html", page="contacto")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
