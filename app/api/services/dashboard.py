
import datetime
from typing import List
from app.api.models.production_model import Production
from app.api.models.products_model import Products
from app.api.models.product_type_model import Product_Type
from peewee import fn
from datetime import datetime, timedelta 
from peewee import JOIN

from app.api.models.shed_model import Shed


def get_products_type_all():
    product_type = (
        Products
        .select(Product_Type.name, fn.COUNT(Products.id).alias('value'))  # Seleccionar el nombre y el conteo
        .join(Product_Type, on=(Products.product_type_id == Product_Type.id))  # Hacer el JOIN
        .where(Products.status_id == 1)  # Filtrar por status_id = 1
        .group_by(Product_Type.name)  # Agrupar por el nombre del tipo de producto
        .order_by(Product_Type.name)  # Opcional: ordenar por nombre
        .dicts()  # Convertir los resultados a diccionarios
    )
    return list(product_type)  # Devolver como lista de diccionarios

def get_productions_type_all():
    production_grafic = (
        Production
        .select(
            fn.SUM(Production.defective_eggs).alias('total_defective_eggs'),
            fn.SUM(Production.quantity).alias('total_quantity'),
            fn.SUM(Production.cull_hens).alias('total_cull_hens'),
            fn.DATE_FORMAT(Production.production_date, '%Y-%m').alias('month')  # Agrupación por mes
        )
        .where(Production.status_id == 1)
        .group_by(fn.DATE_FORMAT(Production.production_date, '%Y-%m'))  # Agrupación
    )
    return list(production_grafic.dicts())

def get_total_hens(filter_type='today'):
    today = datetime.now().date()
    query = (
        Shed
        .select(
            Shed.name_shed.alias('galpon'),
            (Shed.total_hens - fn.IFNULL(fn.SUM(Production.cull_hens), 0)).alias('total_actual_gallinas')
        )
        .join(Production, JOIN.LEFT_OUTER, on=(Shed.id == Production.shed_id))
    )

    # Aplicar el filtro según el parámetro filter_type
    if filter_type == 'today':
        query = query.where(fn.DATE(Production.production_date) == today)
    elif filter_type == 'this_week':
        start_of_week = today - timedelta(days=today.weekday())
        query = query.where(fn.DATE(Production.production_date) >= start_of_week)
    elif filter_type == 'this_month':
        query = query.where(fn.MONTH(Production.production_date) == today.month)

    query = query.group_by(Shed.id).dicts()
    return list(query)