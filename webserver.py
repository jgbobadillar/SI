from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/inicio", methods=['get', 'post'])
def form():
	nombre = request.form.get("nombre")
	edad = request.form.get('edad')
	return render_template("Bienvenido.html", nombre=nombre, edad=edad)

@app.route("/") 
def bienvenido():
	return render_template("form.html")


if __name__ == '__main__':
	app.run()

