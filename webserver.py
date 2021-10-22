from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/") 
def bienvenido():
	return "pagina de arranque"

@app.route("/servicio")
def servicio_ai():
	return "Info de ia"

@app.route("/ruta_servicio")
def ruta_servicio():
	return "Info de ruta de servicio"

@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/inicio", methods=["post"])
def inicio():
	nombre = request.form.get("nombre")
	edad = request.form.get("edad")
	return (f"se recibió {nombre} y {edad}")

@app.route("/productos", methods=["get"])
def devolver_productos():
	print("consultando bases de datos")
	return {"productos": "todos los productos"}

@app.route("/producto/<id>", methods=["get"])
def devolver_product(id):
	print(f"buscando producto {id} en bd")
	return {"nombre": "xxx", "id": id}

@app.route("/producto/crear", methods=["post"])
def crear_producto():
	codigo = request.form.get("codigo")
	nombre = request.form.get("nombre")
	print(f"creando producto {codigo}-{nombre} en la bd")
	return {"status": "OK"}

@app.route("/producto/editar/<id>", methods=["put"])
def editar_producto(id):
        codigo = request.form.get("codigo")
        nombre = request.form.get("nombre")
        print(f"editando producto {id}{codigo}-{nombre} en la bd")
        return {"status": "OK"}

@app.route("/producto/borrar/<id>", methods=["delete"])
def borrar_producto(id):
        print(f"borrando producto {id}en la bd")
        return {"status": "OK"}



if __name__ == '__main__':
	app.run("0.0.0.0")

