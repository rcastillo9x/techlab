# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float

productos = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/productos/")
def create_producto(producto: Producto):
    if producto.id in productos:
        raise HTTPException(status_code=400, detail="Producto ya registrado")
    productos[producto.id] = producto
    return {**producto.dict(), "fecha_peticion": datetime.now(), "hora_peticion": datetime.now().strftime("%H:%M:%S")}

@app.get("/productos/{producto_id}")
def read_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos[producto_id]

@app.put("/productos/{producto_id}")
def update_producto(producto_id: int, producto: Producto):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    productos[producto_id] = producto
    return producto

@app.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    del productos[producto_id]
    return {"detail": "Producto eliminado"}

if __name__ == "__main__":
    import uvicorn
    port = os.getenv("PORT", 8000)
    uvicorn.run(app, host="0.0.0.0", port=int(port))
