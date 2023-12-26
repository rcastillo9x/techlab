import tornado.ioloop
import tornado.web
import json
from datetime import datetime
import os

# Simulando una base de datos en memoria
productos = {}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hola, mundo desde Tornado")

class ProductoHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        productos[data['id']] = data
        data['fecha_peticion'] = datetime.now().isoformat()
        data['hora_peticion'] = datetime.now().strftime("%H:%M:%S")
        self.write(data)

    def get(self, producto_id):
        producto_id = int(producto_id)
        producto = productos.get(producto_id)
        if producto:
            self.write(producto)
        else:
            self.set_status(404)
            self.write({'mensaje': 'Producto no encontrado'})

    def put(self, producto_id):
        producto_id = int(producto_id)
        if producto_id in productos:
            data = json.loads(self.request.body)
            productos[producto_id].update(data)
            self.write({'mensaje': 'Producto actualizado'})
        else:
            self.set_status(404)
            self.write({'mensaje': 'Producto no encontrado'})

    def delete(self, producto_id):
        producto_id = int(producto_id)
        if producto_id in productos:
            del productos[producto_id]
            self.write({'mensaje': 'Producto eliminado'})
        else:
            self.set_status(404)
            self.write({'mensaje': 'Producto no encontrado'})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/productos", ProductoHandler),
        (r"/productos/([0-9]+)", ProductoHandler),
    ])

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
