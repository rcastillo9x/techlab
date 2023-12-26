import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from datetime import datetime
import os
import json

# Simulando una base de datos en memoria
productos = {}

async def create_producto(request):
    data = await request.json()
    productos[data['id']] = data
    data['fecha_peticion'] = datetime.now().isoformat()
    data['hora_peticion'] = datetime.now().strftime("%H:%M:%S")
    return JSONResponse(data)

async def read_producto(request):
    producto_id = int(request.path_params['id'])
    producto = productos.get(producto_id)
    if producto:
        return JSONResponse(producto)
    return JSONResponse({'mensaje': 'Producto no encontrado'}, status_code=404)

async def update_producto(request):
    producto_id = int(request.path_params['id'])
    if producto_id in productos:
        data = await request.json()
        productos[producto_id].update(data)
        return JSONResponse({'mensaje': 'Producto actualizado'})
    return JSONResponse({'mensaje': 'Producto no encontrado'}, status_code=404)

async def delete_producto(request):
    producto_id = int(request.path_params['id'])
    if producto_id in productos:
        del productos[producto_id]
        return JSONResponse({'mensaje': 'Producto eliminado'})
    return JSONResponse({'mensaje': 'Producto no encontrado'}, status_code=404)

routes = [
    Route('/productos', create_producto, methods=['POST']),
    Route('/productos/{id:int}', read_producto, methods=['GET']),
    Route('/productos/{id:int}', update_producto, methods=['PUT']),
    Route('/productos/{id:int}', delete_producto, methods=['DELETE']),
]

app = Starlette(debug=True, routes=routes)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)
