from django.urls import path
from .views import producto_view

urlpatterns = [
    path('productos/', producto_view),
    path('productos/<int:producto_id>/', producto_view),
]
