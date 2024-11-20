from flask import render_template, redirect, request, url_for, jsonify,flash
from models.Productos import Producto
from models.Ingredientes import Ingrediente
from models.Heladeria import Heladeria
from models.Ventas import Venta
from utils.db import db

heladeria = Heladeria()

def principal_routes(app):
    @app.route("/")
    def index():
       productos = None
       productos = Producto.query.limit(4).all()
       return render_template('index.html', productos=productos or " - ")
    
    @app.route("/mostrar_ingredientes")
    def mostrar_ingredientes():    
       ingredientes = Ingrediente.query.all()
       return render_template('mostrar_ingredientes.html', ingredientes=ingredientes)
    
    @app.route('/ingredientes_sanos')
    def mostrar_ingrediente_sano():
        ingredientes = Ingrediente.query.all()  # Obtiene todos los ingredientes
        ingredientes_sanos = []

        # Validar si cada ingrediente es sano
        for ingrediente in ingredientes:
            es_sano = ingrediente.calorias < 100 or ingrediente.es_vegetariano
            ingredientes_sanos.append({
                "nombre": ingrediente.nombre,
                "calorias": ingrediente.calorias,
                "descripcion": ingrediente.descripcion,
                "es_sano": es_sano
            })

        return render_template('ingredientes_sanos.html', ingredientes=ingredientes_sanos)
    
    @app.route('/costo_ajustado')
    def mostrar_costo_ajustado():
        productos = None
        productos = Producto.query.limit(4).all()
        heladeria.productos= []
        for producto in productos:
            costo_total = 0
            for ingrediente_id in [producto.ingrediente1_id, producto.ingrediente2_id, producto.ingrediente3_id]:
                if ingrediente_id:
                    ingrediente = Ingrediente.query.get(ingrediente_id)
                    if ingrediente.nombre:
                        costo_total += ingrediente.precio
            # Agregar los datos del producto con el costo ajustado a la lista
            heladeria.productos.append({
                'nombre': producto.nombre,
                'tipo_vaso': producto.tipo_vaso,
                'costo_ajustado': round(costo_total, 2)
            })

        return render_template('costo_ajustado.html', productos= heladeria.obtener_productos() or " - ")

    @app.route('/calorias')
    def calcular_calorias():
        productos = Producto.query.limit(4).all()
        heladeria.productos= []
        for producto in productos:
            costo_total_calorias = 0
            for ingrediente_id in [producto.ingrediente1_id, producto.ingrediente2_id, producto.ingrediente3_id]:
                if ingrediente_id:
                    ingrediente = Ingrediente.query.get(ingrediente_id)
                    if ingrediente.nombre:
                            costo_total_calorias += ingrediente.calorias * 0.95
                        
            heladeria.productos.append({
                'nombre': producto.nombre,
                'tipo_vaso': producto.tipo_vaso,
                'calorias_totales': round(costo_total_calorias,2)
            })

        return render_template('calorias.html', productos= heladeria.obtener_productos())
    
    @app.route('/rentabilidad')
    def calcular_rentabilidad():
        productos = Producto.query.limit(4).all()
        heladeria.productos= []
        for producto in productos:
            total_ingredientes = 0
            for ingrediente_id in [producto.ingrediente1_id, producto.ingrediente2_id, producto.ingrediente3_id]:
                if ingrediente_id:
                    ingrediente = Ingrediente.query.get(ingrediente_id)
                    if ingrediente:
                            total_ingredientes += ingrediente.precio
                            costo_rentabilidad = ((producto.precio_publico - total_ingredientes) / total_ingredientes)*100            
            heladeria.productos.append({
                'nombre': producto.nombre,
                'tipo_vaso': producto.tipo_vaso,
                'rentabilidad': round(costo_rentabilidad ,2)
            })

        return render_template('rentabilidad.html', productos= heladeria.obtener_productos())

    @app.route('/mas_rentable')
    def mas_rentable():
        productos = Producto.query.limit(4).all()
        producto_rentable = None
        rentabilidad_mayor = float('-inf')
        heladeria.productos= []
        for producto in productos:
            costo_total = 0
            total_ingredientes = 0
            for ingrediente_id in [producto.ingrediente1_id, producto.ingrediente2_id, producto.ingrediente3_id]:
                if ingrediente_id:
                    ingrediente = Ingrediente.query.get(ingrediente_id)
                    if ingrediente:
                        costo_total += ingrediente.precio
                    if costo_total > 0:
                       rentabilidad = ((producto.precio_publico - costo_total) / costo_total) * 100
                    else:
                        rentabilidad = 0 
                    if rentabilidad > rentabilidad_mayor:
                        rentabilidad_mayor = rentabilidad                                 
                    producto_rentable = {
                        'nombre': producto.nombre,
                        'tipo_vaso': producto.tipo_vaso,
                        'precio': producto.precio_publico,
                        'costo_total': round(costo_total, 2),
                        'rentabilidad': round(rentabilidad, 2)
                    }

        return render_template('mas_rentable.html', producto=producto_rentable)
    
    @app.route('/registrar_venta', methods=['GET'])
    def mostrar_registro_venta():
        productos = Producto.query.limit(4).all()  # Obtiene todos los productos
        return render_template('registrar_venta.html', productos=productos)
    
    @app.route('/registrar_venta', methods=['POST'])
    def registrar_venta():
        producto_id = request.form.get('producto_id', type=int)
        cantidad = request.form.get('cantidad', type=int)

        # Registrar la venta en la base de datos
        producto = Producto.query.get(producto_id)
        if not producto:
            flash("Producto no encontrado.", "error")
            return redirect(url_for('mostrar_registro_venta'))

        if producto:
            nueva_venta = Venta(producto_id=producto.id, cantidad=cantidad)
            db.session.add(nueva_venta)
            db.session.commit()
            flash(f'Venta registrada', 'success')
            # Actualizar las ventas totales del producto (opcional)
            producto.ventas_totales = (producto.ventas_totales or 0) + cantidad
            db.session.commit()

            return redirect(url_for('mostrar_registro_venta'))
        else:
            return "Producto no encontrado", 404

    @app.route('/ventas')
    def mostrar_ventas():
        ventas = Venta.query.all()
        return render_template('ventas.html', ventas=ventas)

    @app.route('/ingredientes_categoria')
    def ingredientes_categoria():
        ingredientes = Ingrediente.query.all()  # Obtiene todos los ingredientes
        ingredientes_clasificados = []

        # Validar cada ingrediente
        for ingrediente in ingredientes:
            if ingrediente.calorias < 100 or ingrediente.es_vegetariano:
                categoria = "Es sano"
            else:
                categoria = "No es Sano"

            ingredientes_clasificados.append({
                "nombre": ingrediente.nombre,
                "calorias": ingrediente.calorias,
                "es_vegetariano": ingrediente.es_vegetariano,
                "categoria": categoria
            })

        return render_template('ingredientes_categoria.html', ingredientes=ingredientes_clasificados)
    
    @app.route('/producto_mas_vendido')
    def producto_mas_vendido():
    # Calcular el producto más vendido
        producto = Producto.query.order_by(Producto.ventas_totales.desc()).first()
        
        if producto:
            return render_template('producto_mas_vendido.html', producto=producto)
        else:
            return render_template('producto_mas_vendido.html', producto=None)
    
    @app.route('/abastecer_inventario', methods=['GET', 'POST'])
    def abastecer_inventario():
        if request.method == 'POST':
            ingrediente_id = request.form.get('ingrediente_id')
            heladeria.inventario = int(request.form.get('inventario'))
            
            # Obtener el ingrediente por ID
            ingrediente = Ingrediente.query.get(ingrediente_id)
            if ingrediente:
                ingrediente.inventario += heladeria.inventario  # Sumar la cantidad al inventario
                db.session.commit()
                flash(f'Se abasteció {heladeria.inventario} unidades del ingrediente "{ingrediente.nombre}".', 'success')
            else:
                flash('Ingrediente no encontrado.', 'error')
            
            return redirect(url_for('abastecer_inventario'))
        
        ingredientes = Ingrediente.query.all()
        return render_template('abastecer_inventario.html', ingredientes=ingredientes)
        
    @app.route('/renovar_inventario', methods=['GET', 'POST'])
    def renovar_inventario():
        if request.method == 'POST':
            ingrediente_id = request.form.get('ingrediente_id')
            
            # Buscar el ingrediente por su ID
            ingrediente = Ingrediente.query.get(ingrediente_id)
            if ingrediente:
                ingrediente.inventario = 0  # Establecer inventario a 0
                db.session.commit()
                flash(f'Inventario del ingrediente "{ingrediente.nombre}" renovado a 0.', 'success')
            else:
                flash('Ingrediente no encontrado.', 'error')
            
            return redirect(url_for('renovar_inventario'))
        
        ingredientes = Ingrediente.query.all()
        return render_template('renovar_inventario.html', ingredientes=ingredientes)

    @app.route('/vender/<int:producto_id>', methods=['POST'])
    def vender_producto(producto_id):
        # Obtener el producto desde la lista de productos (simulación)
        producto = next((p for p in heladeria.productos if p.id == producto_id), None)
        
        if not producto:
            flash("Producto no encontrado.", "error")
            return redirect(url_for('vender_productos'))
        else:
            try:
                # Intentar vender el producto
                mensaje = heladeria.vender(producto)
                flash(mensaje, "success")
            except ValueError as e:
                # Capturar el error y mostrar el mensaje personalizado
                flash(f"¡Oh no! Nos hemos quedado sin {str(e)}", "error")

        return redirect(url_for('vender_productos'))   

    @app.route('/vender_producto', methods=['GET', 'POST'])
    def vender_productos():
        productos = Producto.query.limit(4).all()
        ventas = Venta.query.all()
        return render_template('vender_producto.html', productos=productos, ventas=ventas, mensaje=None)

    

    @app.route('/registrar_ventas/<int:producto_id>', methods=['POST'])
    def registrar_ventas(producto_id):
        # Buscar el producto
        productos = Producto.query.limit(4).all()
        producto = next((p for p in heladeria.productos if p.id == producto_id), None)

        if not producto:
            return render_template('vender_producto.html', productos=heladeria.productos, mensaje="Producto no encontrado.")

        try:
            # Intentar registrar la venta
            mensaje = heladeria.vender(producto)
        except ValueError as e:
            # Capturar error si falta ingrediente
            mensaje = f"¡Oh no! Nos hemos quedado sin {str(e)}."

        # Renderizar el resultado
        return render_template('vender_producto.html', mensaje=mensaje)

