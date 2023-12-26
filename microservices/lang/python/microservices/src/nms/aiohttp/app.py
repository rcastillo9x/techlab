from aiohttp import web
import json
from datetime import datetime

# Simulando una base de datos en memoria
productos = {}

async def create_producto(request):
    data = await request.json()
    productos[data['id']] = data
    data['fecha_peticion'] = datetime.now().isoformat()
    data['hora_peticion'] = datetime.now().strftime("%H:%M:%S")
    return web.json_response(data)

async def read_producto(request):
    producto_id = int(request.match_info['id'])
    producto = productos.get(producto_id)
    if producto:
        return web.json_response(producto)
    return web.json_response({'mensaje': 'Producto no encontrado'}, status=404)

async def update_producto(request):
    producto_id = int(request.match_info['id'])
    if producto_id in productos:
        data = await request.json()
        productos[producto_id].update(data)
        return web.json_response({'mensaje': 'Producto actualizado'})
    return web.json_response({'mensaje': 'Producto no encontrado'}, status=404)

async def delete_producto(request):
    producto_id = int(request.match_info['id'])
    if producto_id in productos:
        del productos[producto_id]
        return web.json_response({'mensaje': 'Producto eliminado'})
    return web.json_response({'mensaje': 'Producto no encontrado'}, status=404)

app = web.Application()
app.router.add_post('/productos', create_producto)
app.router.add_get('/productos/{id}', read_producto)
app.router.add_put('/productos/{id}', update_producto)
app.router.add_delete('/productos/{id}', delete_producto)

if __name__ == '__main__':
    web.run_app(app, port=8080)
