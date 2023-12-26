from django.http import JsonResponse
from .models import Producto
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

@csrf_exempt
def producto_view(request, producto_id=None):
    if request.method == 'GET':
        if producto_id:
            try:
                producto = Producto.objects.get(pk=producto_id)
                response_data = {
                    'nombre': producto.nombre,
                    'descripcion': producto.descripcion,
                    'precio': producto.precio,
                    'fecha_peticion': datetime.now().isoformat(),
                    'hora_peticion': datetime.now().strftime("%H:%M:%S")
                }
                return JsonResponse(response_data)
            except Producto.DoesNotExist:
                return JsonResponse({'mensaje': 'Producto no encontrado'}, status=404)
        else:
            productos = list(Producto.objects.values())
            return JsonResponse({'productos': productos})

    elif request.method == 'POST':
        data = json.loads(request.body)
        producto = Producto.objects.create(**data)
        response_data = {**data, 'fecha_peticion': datetime.now().isoformat(), 'hora_peticion': datetime.now().strftime("%H:%M:%S")}
        return JsonResponse(response_data, status=201)

    elif request.method == 'PUT' and producto_id:
        data = json.loads(request.body)
        try:
            producto = Producto.objects.get(pk=producto_id)
            for key, value in data.items():
                setattr(producto, key, value)
            producto.save()
            return JsonResponse({'mensaje': 'Producto actualizado'})
        except Producto.DoesNotExist:
            return JsonResponse({'mensaje': 'Producto no encontrado'}, status=404)

    elif request.method == 'DELETE' and producto_id:
        try:
            producto = Producto.objects.get(pk=producto_id)
            producto.delete()
            return JsonResponse({'mensaje': 'Producto eliminado'})
        except Producto.DoesNotExist:
            return JsonResponse({'mensaje': 'Producto no encontrado'}, status=404)
