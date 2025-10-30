from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", "").strip())
            num2 = float(request.form.get("num2", "").strip())
            operacion = request.form.get("operacion", "suma")

            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                if num2 == 0:
                    error = "No se puede dividir entre cero."
                else:
                    resultado = num1 / num2
        except ValueError:
            error = "Por favor ingrese números válidos."

    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Para desarrollo local:
    app.run(host="0.0.0.0", port=port, debug=True)
