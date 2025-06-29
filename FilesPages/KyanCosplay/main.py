import mysql.connector
import decimal
from datetime import date
from datetime import date, datetime
import getpass
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import uuid

# Conexión a la base de datos
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kyan_cosplay"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print(f"❌ Error al conectar con la base de datos: {err}")
    exit()

##############################
### AUTENTICACIÓN Y ROLES  ###
##############################

def login(cursor):
    print("\n🔐 INICIO DE SESIÓN")
    username = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")

    cursor.execute(
        "SELECT id, username, rol FROM usuarios WHERE username = %s AND password = %s",
        (username, password)
    )
    user = cursor.fetchone()
    if user:
        print(f"✅ Bienvenido, {user[1]} (Rol: {user[2]})")
        return {"id": user[0], "username": user[1], "rol": user[2]}
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return None

def registrar_usuario(cursor, db):
    print("\n📝 REGISTRO DE NUEVO USUARIO")
    while True:
        username = input("Nuevo nombre de usuario: ")
        cursor.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
        if cursor.fetchone():
            print("❌ Ese usuario ya existe. Elige otro.")
        else:
            break
    password = getpass.getpass("Contraseña: ")
    while True:
        print("Roles disponibles: admin, moderador, empleado")
        rol = input("Rol para el nuevo usuario: ").strip().lower()
        if rol in ['admin', 'moderador', 'empleado']:
            break
        else:
            print("❌ Rol no válido.")
    cursor.execute(
        "INSERT INTO usuarios (username, password, rol) VALUES (%s, %s, %s)",
        (username, password, rol)
    )
    db.commit()
    print(f"✅ Usuario '{username}' registrado como '{rol}'.")

##############################
### FUNCIONES DE GESTIÓN   ###
##############################

def agregar_cliente():
    try:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        dni = input("DNI: ")
        cursor.execute("""
            INSERT INTO clientes (Nombre, Apellidos, telefono, email, dni)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellidos, telefono, email, dni))
        db.commit()
        print("✅ Cliente añadido correctamente.\n")
    except Exception as e:
        print(f"❌ Error al añadir cliente: {e}")

def listar_clientes():
    try:
        cursor.execute("SELECT * FROM clientes")
        for cliente in cursor.fetchall():
            print(cliente)
    except Exception as e:
        print(f"❌ Error al listar clientes: {e}")

def editar_cliente():
    try:
        id_cliente = input("ID del cliente a editar: ")
        campo = input("Campo a editar (Nombre, Apellidos, telefono, email, dni): ")
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        cursor.execute(f"UPDATE clientes SET {campo} = %s WHERE id = %s", (nuevo_valor, id_cliente))
        db.commit()
        print("✅ Cliente actualizado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al editar cliente: {e}")

def eliminar_cliente():
    try:
        id_cliente = input("ID del cliente a eliminar: ")
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        db.commit()
        print("✅ Cliente eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al eliminar cliente: {e}")

##############################
### GESTIÓN DE EMPRESA     ###
##############################

def ver_empresa():
    try:
        cursor.execute("SELECT * FROM empresa LIMIT 1")
        empresa = cursor.fetchone()
        if empresa:
            print(f"\nEmpresa: {empresa[1]}\nDirección: {empresa[2]}\nTeléfono: {empresa[3]}\nEmail: {empresa[4]}\nCIF: {empresa[5]}")
        else:
            print("No hay datos de empresa registrados.")
    except Exception as e:
        print(f"❌ Error al consultar la empresa: {e}")

def editar_empresa():
    try:
        cursor.execute("SELECT * FROM empresa LIMIT 1")
        empresa = cursor.fetchone()
        if not empresa:
            print("No hay datos de empresa. Añadiendo nueva empresa.")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            cif = input("CIF: ")
            cursor.execute("INSERT INTO empresa (nombre, direccion, telefono, email, cif) VALUES (%s, %s, %s, %s, %s)", (nombre, direccion, telefono, email, cif))
        else:
            print("Editando datos de la empresa actual:")
            nombre = input(f"Nombre [{empresa[1]}]: ") or empresa[1]
            direccion = input(f"Dirección [{empresa[2]}]: ") or empresa[2]
            telefono = input(f"Teléfono [{empresa[3]}]: ") or empresa[3]
            email = input(f"Email [{empresa[4]}]: ") or empresa[4]
            cif = input(f"CIF [{empresa[5]}]: ") or empresa[5]
            cursor.execute("UPDATE empresa SET nombre=%s, direccion=%s, telefono=%s, email=%s, cif=%s WHERE id=%s", (nombre, direccion, telefono, email, cif, empresa[0]))
        db.commit()
        print("✅ Datos de empresa actualizados.")
    except Exception as e:
        print(f"❌ Error al editar la empresa: {e}")

def menu_empresa():
    while True:
        print("\n🏢 GESTIÓN DE EMPRESA")
        print("1. Ver datos de la empresa")
        print("2. Editar datos de la empresa")
        print("3. Volver")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            ver_empresa()
        elif opcion == '2':
            editar_empresa()
        elif opcion == '3':
            break
        else:
            print("❌ Opción no válida.")

##############################
### GESTIÓN DE PRODUCTOS   ###
##############################

def agregar_producto():
    try:
        tipo = input("Tipo de producto: ")
        codigo = input("Código del producto: ")
        precio = float(input("Precio: "))
        iva = float(input("IVA (%): "))
        stock = int(input("Stock: "))
        descuento = float(input("Descuento (%): "))
        descripcion = input("Descripción: ")
        cursor.execute("""
            INSERT INTO productos (tipodeproducto, codigoproducto, precio, iva, stock, descuento, descripcion)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (tipo, codigo, precio, iva, stock, descuento, descripcion))
        db.commit()
        print("✅ Producto añadido correctamente.\n")
    except Exception as e:
        print(f"❌ Error al añadir producto: {e}")

def listar_productos():
    try:
        cursor.execute("SELECT * FROM productos")
        for producto in cursor.fetchall():
            print(producto)
    except Exception as e:
        print(f"❌ Error al listar productos: {e}")

def editar_producto():
    try:
        id_producto = input("ID del producto a editar: ")
        campo = input("Campo a editar (tipodeproducto, codigoproducto, precio, iva, stock, descuento, descripcion): ")
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        cursor.execute(f"UPDATE productos SET {campo} = %s WHERE id = %s", (nuevo_valor, id_producto))
        db.commit()
        print("✅ Producto actualizado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al editar producto: {e}")

def eliminar_producto():
    try:
        id_producto = input("ID del producto a eliminar: ")
        cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
        db.commit()
        print("✅ Producto eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al eliminar producto: {e}")

##############################
### GESTIÓN DE TALLERES    ###
##############################

def agregar_taller():
    try:
        nombre = input("Nombre del taller: ")
        dia = input("Día (YYYY-MM-DD): ")
        hora = input("Hora (HH:MM:SS): ")
        plazas_totales = int(input("Plazas totales: "))
        precio = float(input("Precio: "))
        iva = float(input("IVA (%): "))
        descuento = float(input("Descuento (%): "))
        cursor.execute("""
            INSERT INTO talleres (nombretaller, dia, hora, plazastotales, precio, iva, descuento)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, dia, hora, plazas_totales, precio, iva, descuento))
        db.commit()
        print("✅ Taller añadido correctamente.\n")
    except Exception as e:
        print(f"❌ Error al añadir taller: {e}")

def listar_talleres():
    try:
        cursor.execute("SELECT * FROM talleres")
        for taller in cursor.fetchall():
            print(taller)
    except Exception as e:
        print(f"❌ Error al listar talleres: {e}")

def editar_taller():
    try:
        id_taller = input("ID del taller a editar: ")
        campo = input("Campo a editar (nombretaller, dia, hora, plazastotales, precio, iva, descuento): ")
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        cursor.execute(f"UPDATE talleres SET {campo} = %s WHERE id = %s", (nuevo_valor, id_taller))
        db.commit()
        print("✅ Taller actualizado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al editar taller: {e}")

def eliminar_taller():
    try:
        id_taller = input("ID del taller a eliminar: ")
        cursor.execute("DELETE FROM talleres WHERE id = %s", (id_taller,))
        db.commit()
        print("✅ Taller eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al eliminar taller: {e}")

##############################
### GESTIÓN DE EVENTOS     ###
##############################

def agregar_evento():
    try:
        nombre = input("Nombre del evento: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        horario = input("Horario (HH:MM:SS): ")
        precio = float(input("Precio: "))
        iva = float(input("IVA (%): "))
        cursor.execute("""
            INSERT INTO eventos (nombre, fecha, horario, precio, iva)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, fecha, horario, precio, iva))
        db.commit()
        print("✅ Evento añadido correctamente.\n")
    except Exception as e:
        print(f"❌ Error al añadir evento: {e}")

def listar_eventos():
    try:
        cursor.execute("SELECT * FROM eventos")
        for evento in cursor.fetchall():
            print(evento)
    except Exception as e:
        print(f"❌ Error al listar eventos: {e}")

def editar_evento():
    try:
        id_evento = input("ID del evento a editar: ")
        campo = input("Campo a editar (nombre, fecha, horario, precio, iva): ")
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        cursor.execute(f"UPDATE eventos SET {campo} = %s WHERE id = %s", (nuevo_valor, id_evento))
        db.commit()
        print("✅ Evento actualizado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al editar evento: {e}")

def eliminar_evento():
    try:
        id_evento = input("ID del evento a eliminar: ")
        cursor.execute("DELETE FROM eventos WHERE id = %s", (id_evento,))
        db.commit()
        print("✅ Evento eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al eliminar evento: {e}")

##############################
### GESTIÓN DE PROVEEDORES ###
##############################

def agregar_proveedor():
    try:
        nombreapellidos = input("Nombre y apellidos del proveedor: ")
        razonsocial = input("Razón social: ")
        direccion = input("Dirección: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")
        cif = input("CIF: ")
        cuentabancaria = input("Cuenta bancaria: ")
        iva = input("IVA (%): ")
        mediodepago = input("Medio de pago: ")
        moneda = input("Moneda: ")
        cursor.execute("""
            INSERT INTO proveedores (
                nombreapellidos, razonsocial, direccion, email, telefono, cif, cuentabancaria, iva, mediodepago, moneda
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombreapellidos, razonsocial, direccion, email, telefono, cif, cuentabancaria, iva, mediodepago, moneda))
        db.commit()
        print("✅ Proveedor añadido correctamente.\n")
    except Exception as e:
        print(f"❌ Error al añadir proveedor: {e}") 

def listar_proveedores():
    try:
        cursor.execute("SELECT * FROM proveedores")
        for proveedor in cursor.fetchall():
            print(proveedor)
    except Exception as e:
        print(f"❌ Error al listar proveedores: {e}")

def editar_proveedor():
    try:
        id_proveedor = input("ID del proveedor a editar: ")
        campo = input("Campo a editar (nombre, telefono, email, direccion): ")
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        cursor.execute(f"UPDATE proveedores SET {campo} = %s WHERE id = %s", (nuevo_valor, id_proveedor))
        db.commit()
        print("✅ Proveedor actualizado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al editar proveedor: {e}")

def eliminar_proveedor():
    try:
        id_proveedor = input("ID del proveedor a eliminar: ")
        cursor.execute("DELETE FROM proveedores WHERE id = %s", (id_proveedor,))
        db.commit()
        print("✅ Proveedor eliminado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al eliminar proveedor: {e}")

##############################
### GESTIÓN DE COMPRAS/PEDIDOS ###
##############################

def agregar_compra():
    try:
        print("\n📝 NUEVO PEDIDO DE COMPRA")
        listar_proveedores()
        id_proveedor = input("ID del proveedor: ")
        fecha = input("Fecha de compra (YYYY-MM-DD): ")
        productos = []
        while True:
            listar_productos()
            id_producto = input("ID del producto a comprar: ")
            cantidad = int(input("Cantidad: "))
            precio_unitario = float(input("Precio unitario de compra: "))
            productos.append((id_producto, cantidad, precio_unitario))
            otro = input("¿Agregar otro producto? (s/n): ").lower()
            if otro != 's':
                break
        # Insertar compra
        cursor.execute(
            "INSERT INTO compras (id_proveedor, fecha) VALUES (%s, %s)",
            (id_proveedor, fecha)
        )
        db.commit()
        id_compra = cursor.lastrowid
        # Insertar detalles de compra
        for id_producto, cantidad, precio_unitario in productos:
            cursor.execute(
                "INSERT INTO compras_detalle (id_compra, id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
                (id_compra, id_producto, cantidad, precio_unitario)
            )
            # Actualizar stock del producto
            cursor.execute(
                "UPDATE productos SET stock = stock + %s WHERE id = %s",
                (cantidad, id_producto)
            )
        db.commit()
        print("✅ Pedido de compra registrado correctamente.\n")
    except Exception as e:
        print(f"❌ Error al registrar compra: {e}")

def listar_compras():
    try:
        print("\n📋 LISTADO DE PEDIDOS DE COMPRA")
        cursor.execute("""
            SELECT c.id, p.nombre, c.fecha
            FROM compras c
            JOIN proveedores p ON c.id_proveedor = p.id
            ORDER BY c.fecha DESC
        """)
        compras = cursor.fetchall()
        for compra in compras:
            print(f"ID: {compra[0]}, Proveedor: {compra[1]}, Fecha: {compra[2]}")
            cursor.execute("""
                SELECT d.id_producto, pr.descripcion, d.cantidad, d.precio_unitario
                FROM compras_detalle d
                JOIN productos pr ON d.id_producto = pr.id
                WHERE d.id_compra = %s
            """, (compra[0],))
            detalles = cursor.fetchall()
            for det in detalles:
                print(f"   Producto: {det[1]} (ID: {det[0]}), Cantidad: {det[2]}, Precio unitario: {det[3]}")
    except Exception as e:
        print(f"❌ Error al listar compras: {e}")

def menu_pedidos():
    while True:
        print("\n📦 MENÚ DE PEDIDOS DE COMPRA")
        print("1. Registrar nuevo pedido de compra")
        print("2. Ver pedidos de compra")
        print("3. Volver")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_compra()
        elif opcion == '2':
            listar_compras()
        elif opcion == '3':
            break
        else:
            print("❌ Opción no válida.")


def estadisticas():
    while True:
        print("\n📊 MENÚ DE ESTADÍSTICAS")
        print("1. Productos más vendidos (TOP 10)")
        print("2. Total de clientes registrados y listado")
        print("3. Proveedores (ordenados por compras realizadas)")
        print("4. Productos con menos stock (TOP 10)")
        print("5. Ventas por mes (últimos 12 meses)")
        print("6. Clientes que más compran (TOP 10)")
        print("7. Proveedores con mejor precio medio")
        print("8. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("\n📦 Productos más vendidos (TOP 10):")
            cursor.execute("""
                SELECT pr.descripcion, SUM(d.cantidad) as total_vendido
                FROM ventas_detalle d
                JOIN productos pr ON d.id_producto = pr.id
                GROUP BY d.id_producto
                ORDER BY total_vendido DESC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            if rows:
                for i, (desc, total) in enumerate(rows, 1):
                    print(f"{i}. {desc} - {total} unidades")
            else:
                print("No hay ventas registradas.")

        elif opcion == '2':
            cursor.execute("SELECT COUNT(*) FROM clientes")
            nclientes = cursor.fetchone()[0]
            print(f"\n👥 Total de clientes registrados: {nclientes}")
            cursor.execute("SELECT id, Nombre, Apellidos, email FROM clientes ORDER BY id")
            clientes = cursor.fetchall()
            for c in clientes:
                print(f"ID: {c[0]}, Nombre: {c[1]} {c[2]}, Email: {c[3]}")

        elif opcion == '3':
            print("\n🏢 Proveedores ordenados por compras realizadas (mayor a menor):")
            cursor.execute("""
                SELECT p.id, p.razonsocial, COUNT(c.id) as compras_realizadas
                FROM proveedores p
                LEFT JOIN compras c ON p.id = c.id_proveedor
                GROUP BY p.id
                ORDER BY compras_realizadas DESC
            """)
            proveedores = cursor.fetchall()
            for i, (pid, nombre, compras) in enumerate(proveedores, 1):
                print(f"{i}. {nombre} (ID: {pid}) - {compras} compras")

        elif opcion == '4':
            print("\n📉 Productos con menos stock (TOP 10):")
            cursor.execute("""
                SELECT descripcion, stock
                FROM productos
                ORDER BY stock ASC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            for i, (desc, stock) in enumerate(rows, 1):
                print(f"{i}. {desc} - {stock} unidades")

        elif opcion == '5':
            print("\n📅 Ventas por mes (últimos 12 meses):")
            cursor.execute("""
                SELECT DATE_FORMAT(cabfac.fecha, '%Y-%m') as mes, SUM(linfac.total_linea) as total_ventas
                FROM cabfac
                JOIN linfac ON cabfac.numfac = linfac.numfac
                WHERE cabfac.tipo = 'F'
                GROUP BY mes
                ORDER BY mes DESC
                LIMIT 12
            """)
            rows = cursor.fetchall()
            if rows:
                for mes, total in rows:
                    print(f"{mes}: {total:.2f} €")
            else:
                print("No hay ventas registradas.")

        elif opcion == '6':
            print("\n👑 Clientes que más compran (TOP 10):")
            cursor.execute("""
                SELECT c.id, c.Nombre, c.Apellidos, SUM(linfac.total_linea) as total_gastado
                FROM cabfac
                JOIN clientes c ON cabfac.idcliente = c.id
                JOIN linfac ON cabfac.numfac = linfac.numfac
                WHERE cabfac.tipo = 'F'
                GROUP BY c.id
                ORDER BY total_gastado DESC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            for i, (cid, nombre, apellidos, total) in enumerate(rows, 1):
                print(f"{i}. {nombre} {apellidos} (ID: {cid}) - {total:.2f} € gastados")

        elif opcion == '7':
            print("\n💰 Proveedores con mejor precio medio (TOP 10):")
            cursor.execute("""
                SELECT p.id, p.razonsocial, AVG(d.precio_unitario) as precio_medio
                FROM compras_detalle d
                JOIN compras c ON d.id_compra = c.id
                JOIN proveedores p ON c.id_proveedor = p.id
                GROUP BY p.id
                HAVING COUNT(d.id) > 0
                ORDER BY precio_medio ASC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            for i, (pid, nombre, precio) in enumerate(rows, 1):
                print(f"{i}. {nombre} (ID: {pid}) - Precio medio: {precio:.2f} €")

        elif opcion == '8':
            break
        else:
            print("❌ Opción no válida.")


##############################
### MENÚS POR ROL          ###
##############################

def menu_mantenimientos_admin():
    while True:
        print("\n🛠️ MENÚ DE MANTENIMIENTOS (ADMIN)")
        print("1. Gestión de Clientes")
        print("2. Gestión de Productos")
        print("3. Gestión de Talleres")
        print("4. Gestión de Eventos")
        print("5. Gestión de Proveedores")
        print("6. Gestión de Empresa")
        print("7. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            submenu_clientes_admin()
        elif opcion == '2':
            submenu_productos_admin()
        elif opcion == '3':
            submenu_talleres_admin()
        elif opcion == '4':
            submenu_eventos_admin()
        elif opcion == '5':
            submenu_proveedores_admin()
        elif opcion == '6':
            menu_empresa()
        elif opcion == '7':
            break
        else:
            print("❌ Opción no válida.")

def menu_mantenimientos_moderador():
    while True:
        print("\n🛠️ MENÚ DE MANTENIMIENTOS (MODERADOR)")
        print("1. Gestión de Clientes")
        print("2. Gestión de Productos")
        print("3. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            submenu_clientes_admin()
        elif opcion == '2':
            submenu_productos_admin()
        elif opcion == '3':
            break
        else:
            print("❌ Opción no válida.")

def menu_mantenimientos_empleado():
    while True:
        print("\n🛠️ MENÚ DE MANTENIMIENTOS (EMPLEADO)")
        print("1. Gestión de Clientes")
        print("2. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            submenu_clientes_empleado()
        elif opcion == '2':
            break
        else:
            print("❌ Opción no válida.")

def submenu_clientes_admin():
    while True:
        print("\n👤 Gestión de Clientes (ADMIN/MODERADOR)")
        print("1. Añadir Cliente")
        print("2. Ver Clientes")
        print("3. Editar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            editar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            break
        else:
            print("❌ Opción no válida.")

def submenu_clientes_empleado():
    while True:
        print("\n👤 Gestión de Clientes (EMPLEADO)")
        print("1. Ver Clientes")
        print("2. Eliminar Cliente")
        print("3. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            listar_clientes()
        elif opcion == '2':
            eliminar_cliente()
        elif opcion == '3':
            break
        else:
            print("❌ Opción no válida.")

def submenu_productos_admin():
    while True:
        print("\n📦 Gestión de Productos")
        print("1. Añadir Producto")
        print("2. Ver Productos")
        print("3. Editar Producto")
        print("4. Eliminar Producto")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            editar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            break
        else:
            print("❌ Opción no válida.")

def submenu_talleres_admin():
    while True:
        print("\n🛠️ Gestión de Talleres")
        print("1. Añadir Taller")
        print("2. Ver Talleres")
        print("3. Editar Taller")
        print("4. Eliminar Taller")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_taller()
        elif opcion == '2':
            listar_talleres()
        elif opcion == '3':
            editar_taller()
        elif opcion == '4':
            eliminar_taller()
        elif opcion == '5':
            break
        else:
            print("❌ Opción no válida.")

def submenu_eventos_admin():
    while True:
        print("\n🎪 Gestión de Eventos")
        print("1. Añadir Evento")
        print("2. Ver Eventos")
        print("3. Editar Evento")
        print("4. Eliminar Evento")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_evento()
        elif opcion == '2':
            listar_eventos()
        elif opcion == '3':
            editar_evento()
        elif opcion == '4':
            eliminar_evento()
        elif opcion == '5':
            break
        else:
            print("❌ Opción no válida.")

def submenu_proveedores_admin():
    while True:
        print("\n🏢 Gestión de Proveedores")
        print("1. Añadir Proveedor")
        print("2. Ver Proveedores")
        print("3. Editar Proveedor")
        print("4. Eliminar Proveedor")
        print("5. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_proveedor()
        elif opcion == '2':
            listar_proveedores()
        elif opcion == '3':
            editar_proveedor()
        elif opcion == '4':
            eliminar_proveedor()
        elif opcion == '5':
            break
        else:
            print("❌ Opción no válida.")

#######################
### SUBMENÚ: CONSULTAS ###
#######################

def menu_consultas_admin():
    while True:
        print("\n🔎 CONSULTAS (ADMIN)")
        print("1. Ver Clientes")
        print("2. Ver Proveedores")
        print("3. Ver Productos")
        print("4. Ver Talleres")
        print("5. Ver Eventos")
        print("6. Ver Facturas")
        print("7. Estadísticas")
        print("8. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            listar_clientes()
        elif opcion == '2':
            listar_proveedores()
        elif opcion == '3':
            listar_productos()
        elif opcion == '4':
            listar_talleres()
        elif opcion == '5':
            listar_eventos()
        elif opcion == '6':
            print("Funcionalidad de facturas no implementada.")
        elif opcion == '7':
            estadisticas()
        elif opcion == '8':
            break
        else:
            print("❌ Opción no válida.")

def menu_consultas_moderador():
    while True:
        print("\n🔎 CONSULTAS (MODERADOR)")
        print("1. Ver Clientes")
        print("2. Ver Productos")
        print("3. Ver Proveedores")
        print("4. Ver Talleres")
        print("5. Ver Eventos")
        print("6. Estadísticas")
        print("7. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            listar_clientes()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            listar_proveedores()
        elif opcion == '4':
            listar_talleres()
        elif opcion == '5':
            listar_eventos()
        elif opcion == '6':
            estadisticas()
        elif opcion == '7':
            break
        else:
            print("❌ Opción no válida.")

def menu_consultas_empleado():
    while True:
        print("\n🔎 CONSULTAS (EMPLEADO)")
        print("1. Ver Clientes")
        print("2. Ver Productos")
        print("3. Ver Talleres")
        print("4. Ver Eventos")
        print("5. Estadísticas")
        print("6. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            listar_clientes()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            listar_talleres()
        elif opcion == '4':
            listar_eventos()
        elif opcion == '5':
            estadisticas()
        elif opcion == '6':
            break
        else:
            print("❌ Opción no válida.")



def agregar_compra():
    try:
        print("\n📝 NUEVO ALBARÁN DE COMPRA A PROVEEDOR")
        cursor.execute("SELECT id, razonsocial, cif FROM proveedores")
        proveedores = cursor.fetchall()
        if not proveedores:
            print("No hay proveedores registrados.")
            return
        print("Proveedores disponibles:")
        for p in proveedores:
            print(f"{p[0]}: {p[1]} | CIF: {p[2]}")
        id_proveedor = input("ID del proveedor: ").strip()
        numero_albaran = input("Número de albarán: ").strip()
        # Fecha de compra: por defecto hoy si se deja vacío
        fecha_compra = input("Fecha de compra (YYYY-MM-DD HH:MM:SS, dejar vacío para hoy): ").strip()
        if not fecha_compra:
            fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fecha_recepcion = input("Fecha de recepción (YYYY-MM-DD HH:MM:SS, dejar vacío si no recibida): ").strip()
        estado = input("Estado (por ejemplo: Pendiente, Recibido): ").strip()
        metodo_pago = input("Método de pago: ").strip()
        referencia_proveedor = input("Referencia proveedor (opcional): ").strip()
        subtotal = float(input("Subtotal: "))
        iva = float(input("IVA: "))
        total = float(input("Total: "))
        observaciones = input("Observaciones (opcional): ").strip()

        compra_id = str(uuid.uuid4())
        fecha_recepcion_sql = fecha_recepcion if fecha_recepcion else None
        referencia_proveedor_sql = referencia_proveedor if referencia_proveedor else None
        observaciones_sql = observaciones if observaciones else None

        cursor.execute("""
            INSERT INTO compras (
                id, numero_albaran, id_proveedor, fecha_compra, fecha_recepcion, estado,
                metodo_pago, referencia_proveedor, subtotal, iva, total, observaciones
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            compra_id, numero_albaran, id_proveedor, fecha_compra, fecha_recepcion_sql, estado,
            metodo_pago, referencia_proveedor_sql, subtotal, iva, total, observaciones_sql
        ))
        db.commit()
        print(f"✅ Compra registrada correctamente con ID: {compra_id}")
    except Exception as e:
        print(f"❌ Error al registrar la compra: {e}")

def listar_compras():
    try:
        print("\n📋 LISTADO DE ALBARANES DE COMPRA")
        cursor.execute("""
            SELECT c.id, c.numero_albaran, p.razonsocial, c.fecha_compra, c.estado, c.total
            FROM compras c
            JOIN proveedores p ON c.id_proveedor = p.id
            ORDER BY c.fecha_compra DESC
        """)
        compras = cursor.fetchall()
        for compra in compras:
            print(f"ID: {compra[0]}, Albarán: {compra[1]}, Proveedor: {compra[2]}, Fecha: {compra[3]}, Estado: {compra[4]}, Total: {compra[5]}")
    except Exception as e:
        print(f"❌ Error al listar compras: {e}")

def consultar_compra():
    try:
        compra_id = input("Introduce el ID (UUID) del albarán de compra: ").strip()
        cursor.execute("""
            SELECT c.id, c.numero_albaran, p.razonsocial, c.fecha_compra, c.fecha_recepcion, c.estado, c.metodo_pago,
                   c.referencia_proveedor, c.subtotal, c.iva, c.total, c.observaciones
            FROM compras c
            JOIN proveedores p ON c.id_proveedor = p.id
            WHERE c.id = %s
        """, (compra_id,))
        compra = cursor.fetchone()
        if not compra:
            print("❌ No se encontró ningún albarán con ese ID.")
            return
        print(f"""
ID: {compra[0]}
Número albarán: {compra[1]}
Proveedor: {compra[2]}
Fecha compra: {compra[3]}
Fecha recepción: {compra[4]}
Estado: {compra[5]}
Método de pago: {compra[6]}
Referencia proveedor: {compra[7]}
Subtotal: {compra[8]}
IVA: {compra[9]}
Total: {compra[10]}
Observaciones: {compra[11]}
        """)
    except Exception as e:
        print(f"❌ Error al consultar compra: {e}")

def editar_compra():
    try:
        compra_id = input("Introduce el ID (UUID) del albarán de compra a editar: ").strip()
        # Mostrar campos editables
        campos = [
            "numero_albaran", "id_proveedor", "fecha_compra", "fecha_recepcion", "estado",
            "metodo_pago", "referencia_proveedor", "subtotal", "iva", "total", "observaciones"
        ]
        print("Campos editables:", ", ".join(campos))
        campo = input("¿Qué campo quieres editar?: ").strip()
        if campo not in campos:
            print("❌ Campo no válido.")
            return
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        # Si el campo puede ser NULL y el usuario deja vacío, poner None
        if campo in ["fecha_recepcion", "referencia_proveedor", "observaciones"] and nuevo_valor == "":
            nuevo_valor = None
        cursor.execute(f"UPDATE compras SET {campo} = %s WHERE id = %s", (nuevo_valor, compra_id))
        db.commit()
        print("✅ Albarán actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error al editar compra: {e}")

def eliminar_compra():
    try:
        compra_id = input("Introduce el ID (UUID) del albarán de compra a eliminar: ").strip()
        cursor.execute("DELETE FROM compras WHERE id = %s", (compra_id,))
        db.commit()
        print("✅ Albarán eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar compra: {e}")

def menu_compras():
    while True:
        print("\n📦 MENÚ DE ALBARANES DE COMPRA")
        print("1. Registrar nuevo albarán de compra")
        print("2. Ver todos los albaranes")
        print("3. Consultar un albarán por ID")
        print("4. Editar un albarán")
        print("5. Eliminar un albarán")
        print("6. Volver")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_compra()
        elif opcion == '2':
            listar_compras()
        elif opcion == '3':
            consultar_compra()
        elif opcion == '4':
            editar_compra()
        elif opcion == '5':
            eliminar_compra()
        elif opcion == '6':
            break
        else:
            print("❌ Opción no válida.")
###################
### FACTURACIÓN ###
###################

def crear_factura(usuario=None):
    try:
        print("\n🧾 CREAR FACTURA")
        # Elegir destinatario
        while True:
            tipo_destinatario = input("¿La factura es para un (C)liente o un (P)roveedor? [C/P]: ").strip().lower()
            if tipo_destinatario in ('c', 'p'):
                break
            else:
                print("❌ Opción no válida. Escribe 'C' para cliente o 'P' para proveedor.")

        if tipo_destinatario == 'c':
            # === FACTURA A CLIENTE ===
            cursor.execute("SELECT id, Nombre, Apellidos FROM clientes")
            clientes = cursor.fetchall()
            if not clientes:
                print("No hay clientes registrados.")
                return
            print("Clientes disponibles:")
            for c in clientes:
                print(f"{c[0]}: {c[1]} {c[2]}")
            idcliente = input("ID del cliente: ")
            cursor.execute("SELECT Nombre, Apellidos, telefono, email, dni FROM clientes WHERE id = %s", (idcliente,))
            cliente = cursor.fetchone()
            if not cliente:
                print("Cliente no encontrado.")
                return
            nombre_destinatario = f"{cliente[0]} {cliente[1]}"
            email_destinatario = cliente[3]
            telefono_destinatario = cliente[2]
            doc_destinatario = cliente[4]  # DNI
            idproveedor = None

        else:
            # === FACTURA A PROVEEDOR ===
            cursor.execute("SELECT id, razonsocial, cif, email, telefono FROM proveedores")
            proveedores = cursor.fetchall()
            if not proveedores:
                print("No hay proveedores registrados.")
                return
            print("Proveedores disponibles:")
            for p in proveedores:
                print(f"{p[0]}: {p[1]} | CIF: {p[2]}")
            idproveedor = input("ID del proveedor: ")
            cursor.execute("SELECT razonsocial, cif, email, telefono FROM proveedores WHERE id = %s", (idproveedor,))
            proveedor = cursor.fetchone()
            if not proveedor:
                print("Proveedor no encontrado.")
                return
            nombre_destinatario = proveedor[0]  # Razón social
            email_destinatario = proveedor[2]
            telefono_destinatario = proveedor[3]
            doc_destinatario = proveedor[1]  # CIF
            idcliente = None

        # Obtener datos de empresa
        cursor.execute("SELECT id, nombre, direccion, telefono, email, cif, codigopostal, poblacion, cuentabancaria, formapago FROM empresa LIMIT 1")
        empresa = cursor.fetchone()
        if not empresa:
            print("No hay datos de empresa.")
            return
        id_empresa = empresa[0]
        nombre_empresa = empresa[1]
        direccion_empresa = empresa[2]
        telefono_empresa = empresa[3]
        email_empresa = empresa[4]
        cif_empresa = empresa[5]
        cp_empresa = empresa[6]
        poblacion_empresa = empresa[7]
        cuenta_empresa = empresa[8]
        formapago_empresa = empresa[9]

        # Calcular el siguiente número de factura
        cursor.execute("SELECT MAX(numfac) FROM cabfac")
        max_numfac = cursor.fetchone()[0]
        numfac = (max_numfac or 0) + 1

        productos = []
        while True:
            cursor.execute("SELECT id, descripcion, precio, iva, descuento FROM productos")
            productos_db = cursor.fetchall()
            print("Productos disponibles:")
            for p in productos_db:
                print(f"{p[0]}: {p[1]} | Precio: {p[2]}€ | IVA: {p[3]}% | Desc: {p[4]}%")
            id_producto = input("ID del producto a facturar: ")
            cantidad = int(input("Cantidad: "))
            prod = next((x for x in productos_db if str(x[0]) == id_producto), None)
            if not prod:
                print("Producto no encontrado.")
                continue
            precio_descuento = float(prod[2]) * (1 - int(prod[4])/100)
            total_linea = round(precio_descuento * cantidad * (1 + int(prod[3])/100), 2)
            productos.append({
                "id_producto": id_producto,
                "descripcion": prod[1],
                "precio": float(prod[2]),
                "iva": int(prod[3]),
                "descuento": int(prod[4]),
                "cantidad": cantidad,
                "total_linea": total_linea
            })
            otro = input("¿Agregar otro producto? (s/n): ").lower()
            if otro != 's':
                break

        # Insertar cabecera de factura
        fecha_hoy = date.today()
        cursor.execute("""
            INSERT INTO cabfac (
                numfac, tipo_destinatario, idcliente, idproveedor,
                nombre_destinatario, email_destinatario, telefono_destinatario, doc_destinatario,
                nombreempresa, fecha, tipo
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            numfac,
            'cliente' if tipo_destinatario == 'c' else 'proveedor',
            idcliente,
            idproveedor,
            nombre_destinatario,
            email_destinatario,
            telefono_destinatario,
            doc_destinatario,
            id_empresa,
            fecha_hoy,
            'F'
        ))
        db.commit()

        # Insertar líneas de factura
        for prod in productos:
            cursor.execute("""
                INSERT INTO linfac (numfac, id_producto, descripcion, precio, unidad, iva, descuento, total_linea)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                numfac, prod["id_producto"], prod["descripcion"], prod["precio"],
                prod["cantidad"], prod["iva"], prod["descuento"], prod["total_linea"]
            ))
            # Si quieres actualizar stock, puedes hacerlo aquí si aplica
        db.commit()
        print(f"✅ Factura creada correctamente. Número de factura: {numfac}")

        # === Generar PDF ===
        ruta_pdf = generar_factura_pdf(
            numfac=numfac,
            nombre_empresa=nombre_empresa,
            direccion_empresa=direccion_empresa,
            telefono_empresa=telefono_empresa,
            email_empresa=email_empresa,
            cif_empresa=cif_empresa,
            cp_empresa=cp_empresa,
            poblacion_empresa=poblacion_empresa,
            cuenta_empresa=cuenta_empresa,
            formapago_empresa=formapago_empresa,
            nombre_cliente=nombre_destinatario,
            apellidos_cliente="",
            telefono_cliente=telefono_destinatario,
            email_cliente=email_destinatario,
            dni_cliente=doc_destinatario,
            fecha=fecha_hoy,
            productos=productos,
            tipo="F"
        )
        print(f"📄 PDF generado: {ruta_pdf}")

    except Exception as e:
        print(f"❌ Error al crear la factura: {e}")




# ==========================
# FUNCIÓN PARA GENERAR PDF
# ==========================
def generar_factura_pdf(
    numfac,
    nombre_empresa,
    direccion_empresa,
    telefono_empresa,
    email_empresa,
    cif_empresa,
    cp_empresa,
    poblacion_empresa,
    cuenta_empresa,
    formapago_empresa,
    nombre_cliente,
    apellidos_cliente,
    telefono_cliente,
    email_cliente,
    dni_cliente,
    fecha,
    productos,
    tipo="F"
):
    import textwrap

    base_dir = "Facturas"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    if tipo == "A":
        base_dir = os.path.join(base_dir, "Abonos")
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
    nombre_archivo = f"Factura_{numfac}.pdf" if tipo == "F" else f"Abono_{numfac}.pdf"
    ruta_pdf = os.path.join(base_dir, nombre_archivo)

    c = canvas.Canvas(ruta_pdf, pagesize=A4)
    width, height = A4

    margen_izq = 40
    margen_der = width - 260

    # --- Número de factura y fecha (arriba del todo, centrados) ---
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 40, f"{'FACTURA' if tipo == 'F' else 'ABONO'} Nº {numfac}")
    c.setFont("Helvetica", 11)
    c.drawCentredString(width / 2, height - 60, f"Fecha: {fecha.strftime('%d/%m/%Y')}")

    # --- Cabecera: Empresa (izquierda) ---
    y_top = height - 90  # Más abajo para dejar espacio a la cabecera principal

    c.setFont("Helvetica-Bold", 12)
    c.drawString(margen_izq, y_top, nombre_empresa)
    c.setFont("Helvetica", 10)
    c.drawString(margen_izq, y_top - 15, f"Dirección: {direccion_empresa}")
    c.drawString(margen_izq, y_top - 30, f"C.P.: {cp_empresa} - {poblacion_empresa}")
    c.drawString(margen_izq, y_top - 45, f"Teléfono: {telefono_empresa}")
    c.drawString(margen_izq, y_top - 60, f"Email: {email_empresa}")
    c.drawString(margen_izq, y_top - 75, f"CIF: {cif_empresa}")
    c.drawString(margen_izq, y_top - 90, f"Cuenta: {cuenta_empresa}")
    c.drawString(margen_izq, y_top - 105, f"Forma de pago: {formapago_empresa}")

    # --- Cabecera: Cliente (derecha) ---
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margen_der, y_top, "Cliente:")
    c.setFont("Helvetica", 10)
    c.drawString(margen_der, y_top - 15, f"{nombre_cliente} {apellidos_cliente}")
    c.drawString(margen_der, y_top - 30, f"DNI: {dni_cliente}")
    c.drawString(margen_der, y_top - 45, f"Teléfono: {telefono_cliente}")
    c.drawString(margen_der, y_top - 60, f"Email: {email_cliente}")

    # --- Separación visual ---
    y = y_top - 130
    c.setLineWidth(1)
    c.line(margen_izq, y, width - margen_izq, y)
    y -= 20  # Más espacio entre cabecera y tabla

    # --- Tabla de productos ---
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, y, "Descripción")
    c.drawString(220, y, "Cantidad")
    c.drawString(280, y, "Precio")
    c.drawString(340, y, "IVA")
    c.drawString(380, y, "Desc.")
    c.drawString(430, y, "Total línea")
    c.setFont("Helvetica", 10)
    y -= 15

    subtotal = 0
    iva_dict = {}
    for prod in productos:
        descripcion = str(prod["descripcion"])
        descripcion_wrapped = textwrap.wrap(descripcion, width=35)
        for i, linea in enumerate(descripcion_wrapped):
            c.drawString(40, y, linea)
            if i == 0:
                c.drawString(220, y, str(prod["cantidad"]))
                c.drawString(280, y, f"{prod['precio']:.2f}€")
                c.drawString(340, y, f"{prod['iva']}%")
                c.drawString(380, y, f"{prod['descuento']}%")
                c.drawString(430, y, f"{prod['total_linea']:.2f}€")
            y -= 15
            if y < 80:
                c.showPage()
                y = height - 50

        precio_descuento = prod["precio"] * (1 - prod["descuento"]/100)
        base = precio_descuento * prod["cantidad"]
        subtotal += base
        iva_tipo = prod["iva"]
        iva_dict.setdefault(iva_tipo, 0)
        iva_dict[iva_tipo] += base

    # Subtotal
    c.setFont("Helvetica-Bold", 11)
    c.drawString(340, y - 10, "SUBTOTAL:")
    c.drawString(430, y - 10, f"{subtotal:.2f}€")
    y -= 25

    # IVA desglosado
    c.setFont("Helvetica-Bold", 10)
    total_iva = 0
    for iva_tipo, base in sorted(iva_dict.items()):
        iva_valor = base * iva_tipo / 100
        c.drawString(340, y, f"IVA {iva_tipo}%:")
        c.drawString(430, y, f"{iva_valor:.2f}€")
        total_iva += iva_valor
        y -= 15

    # Total
    total_factura = subtotal + total_iva
    c.setFont("Helvetica-Bold", 12)
    c.drawString(340, y - 10, "TOTAL:")
    c.drawString(430, y - 10, f"{total_factura:.2f}€")

    c.save()
    return ruta_pdf

def listar_facturas():
    try:
        print("\n🧾 BUSCAR FACTURA POR NÚMERO")
        numfac = input("Introduce el NÚMERO de la factura que deseas ver (o 'volver' para regresar): ")
        if numfac.strip().lower() == "volver":
            return

        cursor.execute("""
            SELECT c.numfac, c.nombreempresa, c.nombreproveedor, c.direccion, c.fecha
            FROM cabfac c
            WHERE c.tipo = 'F' AND c.numfac = %s
        """, (numfac,))
        factura = cursor.fetchone()
        if not factura:
            print("❌ No se encontró ninguna factura con ese número.")
            return

        print(f"Factura Nº: {factura[0]}, Empresa: {factura[1]}, Cliente: {factura[2]}, Dirección: {factura[3]}, Fecha: {factura[4]}")
        cursor.execute("""
            SELECT l.id_producto, l.descripcion, l.unidad, l.precio, l.iva, l.descuento, l.total_linea
            FROM linfac l
            WHERE l.numfac = %s
        """, (numfac,))
        detalles = cursor.fetchall()
        for det in detalles:
            print(f"   Producto: {det[1]} (ID: {det[0]}), Cantidad: {det[2]}, Precio unitario: {det[3]}, IVA: {det[4]}%, Desc: {det[5]}%, Total línea: {det[6]}")
    except Exception as e:
        print(f"❌ Error al buscar la factura: {e}")


def crear_abono():
    try:
        print("\n🧾 CREAR ABONO (NOTA DE CRÉDITO)")
        numfac_origen = input("Introduce el NÚMERO de la factura a abonar: ").strip()
        # Buscar la factura original
        cursor.execute("""
            SELECT numfac, tipo_destinatario, idcliente, idproveedor, nombre_destinatario, email_destinatario,
                   telefono_destinatario, doc_destinatario, nombreempresa, fecha, tipo
            FROM cabfac WHERE numfac = %s AND tipo = 'F'
        """, (numfac_origen,))
        cab = cursor.fetchone()
        if not cab:
            print("❌ No se encontró ninguna factura con ese número.")
            return

        # Mostrar datos de la factura original
        print(f"\nFactura a abonar: Nº {cab[0]}, Destinatario: {cab[4]}, Fecha: {cab[9]}")
        cursor.execute("""
            SELECT id_producto, descripcion, precio, unidad, iva, descuento, total_linea
            FROM linfac WHERE numfac = %s
        """, (numfac_origen,))
        lineas = cursor.fetchall()
        if not lineas:
            print("❌ La factura no tiene líneas.")
            return
        print("Líneas de la factura:")
        for l in lineas:
            print(f"  Producto: {l[1]}, Cantidad: {l[3]}, Precio: {l[2]}, IVA: {l[4]}%, Desc: {l[5]}%, Total línea: {l[6]}")

        confirm = input("¿Deseas crear el abono de esta factura? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operación cancelada.")
            return

        # Calcular el siguiente número de documento (factura o abono)
        cursor.execute("SELECT MAX(numfac) FROM cabfac")
        max_numfac = cursor.fetchone()[0]
        numabono = (max_numfac or 0) + 1

        # Insertar cabecera de abono (tipo = 'A')
        fecha_hoy = date.today()
        cursor.execute("""
            INSERT INTO cabfac (
                numfac, tipo_destinatario, idcliente, idproveedor,
                nombre_destinatario, email_destinatario, telefono_destinatario, doc_destinatario,
                nombreempresa, fecha, tipo
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            numabono,
            cab[1],  # tipo_destinatario
            cab[2],  # idcliente
            cab[3],  # idproveedor
            cab[4],  # nombre_destinatario
            cab[5],  # email_destinatario
            cab[6],  # telefono_destinatario
            cab[7],  # doc_destinatario
            cab[8],  # nombreempresa
            fecha_hoy,
            'A'
        ))
        db.commit()

        # Insertar líneas de abono (importes negativos)
        productos = []
        for l in lineas:
            cursor.execute("""
                INSERT INTO linfac (numfac, id_producto, descripcion, precio, unidad, iva, descuento, total_linea)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                numabono, l[0], l[1], -abs(l[2]), l[3], l[4], l[5], -abs(l[6])
            ))
            productos.append({
                "id_producto": l[0],
                "descripcion": l[1],
                "precio": -abs(float(l[2])),
                "iva": int(l[4]),
                "descuento": int(l[5]),
                "cantidad": l[3],
                "total_linea": -abs(float(l[6]))
            })
        db.commit()
        print(f"✅ Abono creado correctamente. Número de abono: {numabono} (de la factura {cab[0]})")

        # Obtener datos de empresa para el PDF
        cursor.execute("SELECT nombre, direccion, telefono, email, cif, codigopostal, poblacion, cuentabancaria, formapago FROM empresa LIMIT 1")
        empresa = cursor.fetchone()
        if not empresa:
            print("No hay datos de empresa.")
            return

        # Generar PDF de abono
        ruta_pdf = generar_factura_pdf(
            numfac=numabono,
            nombre_empresa=empresa[0],
            direccion_empresa=empresa[1],
            telefono_empresa=empresa[2],
            email_empresa=empresa[3],
            cif_empresa=empresa[4],
            cp_empresa=empresa[5],
            poblacion_empresa=empresa[6],
            cuenta_empresa=empresa[7],
            formapago_empresa=empresa[8],
            nombre_cliente=cab[4],
            apellidos_cliente="",
            telefono_cliente=cab[6],
            email_cliente=cab[5],
            dni_cliente=cab[7],
            fecha=fecha_hoy,
            productos=productos,
            tipo="A"
        )
        print(f"📄 PDF de abono generado: {ruta_pdf}")

    except Exception as e:
        print(f"❌ Error al crear el abono: {e}")


def submenu_facturacion_admin():
    while True:
        print("\n💼 SUBMENÚ DE FACTURACIÓN")
        print("1. Crear factura")
        print("2. Crear abono (nota de crédito)")
        print("3. Ver facturas")
        print("4. Volver")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            crear_factura()
        elif opcion == '2':
            crear_abono()
        elif opcion == '3':
            listar_facturas()
        elif opcion == '4':
            break
        else:
            print("❌ Opción no válida.")


def menu_estadisticas():
    while True:
        print("\n📊 MENÚ DE ESTADÍSTICAS")
        print("1. Productos más vendidos (TOP 10)")
        print("2. Total de clientes registrados y listado")
        print("3. Proveedores (ordenados por compras realizadas)")
        print("4. Productos con menos stock (TOP 10)")
        print("5. Ventas por mes (últimos 12 meses)")
        print("6. Clientes que más compran (TOP 10)")
        print("7. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("\n📦 Productos más vendidos (TOP 10):")
            cursor.execute("""
                SELECT pr.descripcion, SUM(l.unidad) as total_vendido
                FROM linfac l
                JOIN productos pr ON l.id_producto = pr.id
                GROUP BY l.id_producto
                ORDER BY total_vendido DESC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            if rows:
                for i, (desc, total) in enumerate(rows, 1):
                    print(f"{i}. {desc} - {total} unidades")
            else:
                print("No hay ventas registradas.")

        elif opcion == '2':
            cursor.execute("SELECT COUNT(*) FROM clientes")
            nclientes = cursor.fetchone()[0]
            print(f"\n👥 Total de clientes registrados: {nclientes}")
            cursor.execute("SELECT id, Nombre, Apellidos, email FROM clientes ORDER BY id")
            clientes = cursor.fetchall()
            for c in clientes:
                print(f"ID: {c[0]}, Nombre: {c[1]} {c[2]}, Email: {c[3]}")

        elif opcion == '3':
            print("\n🏢 Proveedores ordenados por compras realizadas (mayor a menor):")
            cursor.execute("""
                SELECT p.id, p.razonsocial, COUNT(c.id) as compras_realizadas
                FROM proveedores p
                LEFT JOIN compras c ON p.id = c.id_proveedor
                GROUP BY p.id
                ORDER BY compras_realizadas DESC
            """)
            proveedores = cursor.fetchall()
            for i, (pid, nombre, compras) in enumerate(proveedores, 1):
                print(f"{i}. {nombre} (ID: {pid}) - {compras} compras")

        elif opcion == '4':
            print("\n📉 Productos con menos stock (TOP 10):")
            cursor.execute("""
                SELECT descripcion, stock
                FROM productos
                ORDER BY stock ASC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            for i, (desc, stock) in enumerate(rows, 1):
                print(f"{i}. {desc} - {stock} unidades")

        elif opcion == '5':
            print("\n📅 Ventas por mes (últimos 12 meses):")
            cursor.execute("""
                SELECT DATE_FORMAT(cabfac.fecha, '%Y-%m') as mes, SUM(linfac.total_linea) as total_ventas
                FROM cabfac
                JOIN linfac ON cabfac.numfac = linfac.numfac
                WHERE cabfac.tipo = 'F'
                GROUP BY mes
                ORDER BY mes DESC
                LIMIT 12
            """)
            rows = cursor.fetchall()
            if rows:
                for mes, total in rows:
                    print(f"{mes}: {total:.2f} €")
            else:
                print("No hay ventas registradas.")

        elif opcion == '6':
            print("\n👑 Clientes que más compran (TOP 10):")
            cursor.execute("""
                SELECT c.id, c.Nombre, c.Apellidos, SUM(linfac.total_linea) as total_gastado
                FROM cabfac
                JOIN clientes c ON cabfac.idcliente = c.id
                JOIN linfac ON cabfac.numfac = linfac.numfac
                WHERE cabfac.tipo = 'F'
                GROUP BY c.id
                ORDER BY total_gastado DESC
                LIMIT 10
            """)
            rows = cursor.fetchall()
            for i, (cid, nombre, apellidos, total) in enumerate(rows, 1):
                print(f"{i}. {nombre} {apellidos} (ID: {cid}) - {total:.2f} € gastados")

        elif opcion == '7':
            break
        else:
            print("❌ Opción no válida.")


#######################
### MENÚ PRINCIPAL  ###
#######################

def menu_principal(usuario):
    while True:
        print(f"\n📍 MENÚ PRINCIPAL ({usuario['rol'].upper()})")
        if usuario['rol'] == 'admin':
            print("1. Mantenimientos")
            print("2. Consultas")
            print("3. Facturación")
            print("4. Pedidos de compra")
            print("5. Estadisticas")
            print("6. Registrar usuario")
            print("7. Cerrar sesión")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                menu_mantenimientos_admin()
            elif opcion == '2':
                menu_consultas_admin()
            elif opcion == '3':
                submenu_facturacion_admin()
            elif opcion == '4':
                menu_pedidos()
            elif opcion == '5':
                menu_estadisticas()
            elif opcion == '6':
                registrar_usuario(cursor, db)
            elif opcion == '7':
                print("🔒 Cerrando sesión...")
                break
            else:
                print("❌ Opción no válida.")

        elif usuario['rol'] == 'moderador':
            print("1. Mantenimientos")
            print("2. Consultas")
            print("3. Pedidos de compra")
            print("4. Cerrar sesión")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                menu_mantenimientos_moderador()
            elif opcion == '2':
                menu_consultas_moderador()
            elif opcion == '3':
                menu_pedidos()
            elif opcion == '4':
                print("🔒 Cerrando sesión...")
                break
            else:
                print("❌ Opción no válida.")

        elif usuario['rol'] == 'empleado':
            print("1. Mantenimientos")
            print("2. Consultas")
            print("3. Pedidos de compra")
            print("4. Cerrar sesión")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                menu_mantenimientos_empleado()
            elif opcion == '2':
                menu_consultas_empleado()
            elif opcion == '3':
                menu_pedidos()
            elif opcion == '4':
                print("🔒 Cerrando sesión...")
                break
            else:
                print("❌ Opción no válida.")

        else:
            print("❌ Rol no reconocido. Cerrando sesión.")
            break

#######################
### INICIO DE SESIÓN ###
#######################

def inicio_sesion():
    while True:
        print("\n1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            usuario = login(cursor)
            if usuario:
                return usuario
        elif opcion == '2':
            print("👋 Saliendo del programa...")
            exit()
        else:
            print("❌ Opción no válida.")

# Ejecutar
if __name__ == "__main__":
    try:
        while True:
            usuario = inicio_sesion()
            menu_principal(usuario)
    finally:
        cursor.close()
        db.close()
        print("🔒 Conexión cerrada.")