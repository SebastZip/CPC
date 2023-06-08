from Administrador import Administrador
from Cliente import Cliente
from Reporte import Reporte
from Ticket import Ticket
from Vehiculo import Vehiculo
from Arbol import *
import numpy as np
import pickle
import os
import datetime

class Sistema:
    def __init__(self, estado):
        self.__estado = estado
        self.__arbolClientes = AVLTree()
        self.__tickets = []
        self.__vehiculos = []

    def buscar_cliente_por_nombre(self, nombre_cliente):
        cliente = self.__arbolClientes.buscar(nombre_cliente)
        if cliente:
            return cliente
        else:
            return None
    
    # Getter para el atributo estado
    def get_estado(self):
        return self.__estado

    # Setter para el atributo estado
    def set_estado(self, estado):
        self.__estado = estado

    def registrarCliente(self, cliente):
        
        # Cargar el árbol de clientes desde el archivo existente
        with open('arbol_clientes.pkl', 'rb') as file:
            self.__arbolClientes = pickle.load(file)

        # Insertar el cliente en el árbol
        self.__arbolClientes.insert(cliente.get_idCliente(), cliente)

        # Guardar el árbol con los clientes en el archivo
        with open('arbol_clientes.pkl', 'wb') as file:
            pickle.dump(self.__arbolClientes, file)
    

    def crearEstacionamiento(self): #Matriz y FILA secuencial
         # Crear una matriz 20x20 llena de ceros
        estacionamiento = np.zeros((20, 20), dtype=int)
        # Guardar la matriz en un archivo
        np.savetxt('estacionamiento.txt', estacionamiento, fmt='%d')


        
    def guardar_datos(self):
        with open("tickets.pkl", "wb") as f:
            pickle.dump(self.__tickets, f)
        with open("vehiculos.pkl", "wb") as f:
            pickle.dump(self.__vehiculos, f)

    def cargar_datos(self):
        try:
            with open("tickets.pkl", "rb") as f:
                self.__tickets = pickle.load(f)
        except FileNotFoundError:
            self.__tickets = []
        try:
            with open("vehiculos.pkl", "rb") as f:
                self.__vehiculos = pickle.load(f)
        except FileNotFoundError:
            self.__vehiculos = []

        # Cargar el árbol de clientes desde el archivo
        try:
            with open("arbol_clientes.pkl", "rb") as f:
                self.__arbolClientes = pickle.load(f)
        except FileNotFoundError:
            self.__arbolClientes = None

    def ingresarVehiculo(self, nombre_cliente, vehiculo):
        cliente = self._buscarClienteEnArbolPorNombre(self.__arbolClientes.root, nombre_cliente)

        if cliente is not None:
            ticket_id = len(self.__tickets) + 1  # Generar el ID del ticket
            horaIngreso = "08:00"  # Hora de ingreso (se puede obtener de forma dinámica)
            fecha = "2023-06-06"  # Fecha actual (se puede obtener de forma dinámica)

            # Crear el objeto Ticket
            ticket = Ticket(ticket_id, horaIngreso, None, fecha, vehiculo, None, None)

            # Agregar el ticket al cliente y vehículo correspondiente
            cliente.get_tickets().append(ticket)
            cliente.get_vehiculos().append(vehiculo)

            # Agregar el ticket a la lista de tickets del sistema
            self.__tickets.append(ticket)
            self.__vehiculos.append(vehiculo)

            # Actualizar el cliente en el árbol de clientes
            self.__arbolClientes.actualizar_cliente(cliente, ticket)

            # Guardar los datos actualizados
            self.guardar_datos()

            print("Vehículo ingresado exitosamente.")
        else:
            print("Cliente no encontrado.")

        


    def liberarVehiculo(self):
        pass

    def generarReporteDiario(self):
        pass

    def verReportes(self):
        pass

    def asignarUbicacion(self):
        pass

    def verEstacionamiento(self):
        # Verificar la existencia del archivo de estacionamiento
        try:
            estacionamiento = np.loadtxt('estacionamiento.txt', dtype=int)
        except IOError:
            print("No se encontro el archivo de estacionamiento.")
            return

        # Obtener las dimensiones de la matriz de estacionamiento
        filas, columnas = estacionamiento.shape
        # Etiquetas para las filas y columnas
        etiquetas_filas = ['f' + str(i) for i in range(filas)]
        
        # Imprimir la matriz de estacionamiento
        print("Estacionamiento:")
        print(" ", end="")
        print()
        for i, fila in enumerate(estacionamiento):
            print(etiquetas_filas[i], end=": ")
            for valor in fila:
                print(valor, end=" ")
            print()

    def validarAdministrador(self,administrador):
         # Leer el archivo de credenciales de administradores
        with open('credenciales_administradores.txt', 'r') as file:
            lineas = file.readlines()

        # Iterar sobre las líneas del archivo
        for linea in lineas:
            # Dividir la línea en usuario, contraseña y llave maestra
            credenciales = linea.strip().split(',')

            # Obtener las credenciales de usuario, contraseña y llave maestra
            usuario_archivo = credenciales[0]
            contrasenia_archivo = credenciales[1]
            llave_maestra_archivo = credenciales[2]

            # Validar las credenciales del administrador
            if administrador.get_usuario() == usuario_archivo and \
               administrador.get_contrasenia() == contrasenia_archivo and \
               administrador.get_llaveMaestra() == llave_maestra_archivo:
                return True
        
        return False

    def validarEspacioEstacionamiento(self):
        pass

    def liberarEstacionamiento(self):
        pass
    
    def limpiarEstacionamiento(self):
        # Verificar la existencia del archivo de estacionamiento
        try:
            estacionamiento = np.loadtxt('estacionamiento.txt', dtype=int)
        except IOError:
            print("No se encontró el archivo de estacionamiento.")
            return
        # Llenar la matriz de estacionamiento con ceros
        estacionamiento.fill(0)
        # Guardar la matriz actualizada en el archivo
        np.savetxt('estacionamiento.txt', estacionamiento, fmt='%d')

    def crearArchivoAdministradores(self):
        # Crear el arreglo de credenciales de administradores
        administradores = [
            {
                "usuario": "admin1",
                "contrasenia": "contrasenia1",
                "llaveMaestra": "llave1",
                "idAdministrador": "admin001"
            },
            {
                "usuario": "admin2",
                "contrasenia": "contrasenia2",
                "llaveMaestra": "llave2",
                "idAdministrador": "admin002"
            },
            # Agrega más elementos al arreglo si es necesario
        ]
        # Guardar el arreglo en un archivo
        with open('credenciales_administradores.txt', 'w') as file:
            for admin in administradores:
                linea = f"{admin['usuario']},{admin['contrasenia']},{admin['llaveMaestra']},{admin['idAdministrador']}\n"
                file.write(linea)

    def _buscarClienteEnArbolPorNombre(self, node, nombre_cliente):
        if node is None:
            return None
        
        if node.value.get_nombre() == nombre_cliente:
            return node.value

        if nombre_cliente < node.value.get_nombre():
            return self._buscarClienteEnArbolPorNombre(node.left, nombre_cliente)
        else:
            return self._buscarClienteEnArbolPorNombre(node.right, nombre_cliente)


    def imprimirClientes(self):
         # Cargar el árbol de clientes desde el archivo
        with open('arbol_clientes.pkl', 'rb') as file:
            self.__arbolClientes = pickle.load(file)

        self.__imprimirArbolClientesRecursivo(self.__arbolClientes.root)

    def __imprimirArbolClientesRecursivo(self, nodo):
        if nodo is not None:
            self.__imprimirArbolClientesRecursivo(nodo.left)

            cliente = nodo.value
            print("ID del cliente:", cliente.get_idCliente())
            print("Nombre del cliente:", cliente.get_nombre())
            print("Contacto del cliente:", cliente.get_contacto())

            print("Tickets del cliente:")
            for ticket in cliente.get_tickets():
                print("ID del ticket:", ticket.get_idTicket())
                print("Hora de ingreso:", ticket.get_horaIngreso())
                print("Hora de salida:", ticket.get_horaSalida())
                print("Fecha:", ticket.get_fecha())
                # Imprimir otros atributos del ticket según corresponda

            print("Vehículos del cliente:")
            for vehiculo in cliente.get_vehiculos():
                print("ID del vehículo:", vehiculo.get_idVehiculo())
                print("Placa del vehículo:", vehiculo.get_placa())
                print("Ubicación del vehículo:", vehiculo.get_ubicacion())
                # Imprimir otros atributos del vehículo según corresponda

            print("----------------------------------")

            self.__imprimirArbolClientesRecursivo(nodo.right)


    def validarCliente(self, nombre_cliente):

        # Cargar el árbol de clientes desde el archivo
        with open('arbol_clientes.pkl', 'rb') as file:
            self.__arbolClientes = pickle.load(file)

        return self.__validar_cliente_en_arbol_recursivo(self.__arbolClientes.root, nombre_cliente)

    def __validar_cliente_en_arbol_recursivo(self, nodo, nombre_cliente):
        if nodo is None:
            return False

        if nodo.value.get_nombre() == nombre_cliente:
            return True

        if nombre_cliente < nodo.value.get_nombre():
            return self.__validar_cliente_en_arbol_recursivo(nodo.left, nombre_cliente)
        else:
            return self.__validar_cliente_en_arbol_recursivo(nodo.right, nombre_cliente)



def main():
    # Crear una instancia del sistema
    sistema = Sistema(estado="Activo")
    #administrador = Administrador("admin2", "contrasenia2", "llave2", "admin002")
    #accesoAdmi = sistema.validarAdministrador(administrador)
    #print(accesoAdmi)
    #sistema.verEstacionamiento()
    #sistema.limpiarEstacionamiento()
    #sistema.ingresarVehiculo(cliente, vehiculo)
    #sistema.imprimirClientes()
    #Registrar un cliente
    cliente = Cliente(idCliente="2", nombre="Rose", contacto="jennie@example.com",
                  vehiculos=[], tickets=[], prioridad=3)
    # Agregar tickets de prueba al cliente
    #ticket1 = Ticket(idTicket="T005", horaIngreso="08:00", horaSalida=None, fecha="2023-06-06",
    #                vehiculo=None, monto=None, horasTotales=None)
    #ticket2 = Ticket(idTicket="T002", horaIngreso="09:30", horaSalida=None, fecha="2023-06-06",
    #                vehiculo=None, monto=None, horasTotales=None)
    #cliente.get_tickets().append(ticket1)
    #cliente.get_tickets().append(ticket2)
    # Agregar vehículos de prueba al cliente
    #vehiculo1 = Vehiculo(idVehiculo="V005", placa="BPA123", ubicacion="Piso 5")
    #vehiculo2 = Vehiculo(idVehiculo="V002", placa="XYZ789", ubicacion="Piso 1")
    #cliente.get_vehiculos().append(vehiculo1)
    #cliente.get_vehiculos().append(vehiculo2)
    # Registrar el cliente en el sistema
    sistema.registrarCliente(cliente)
    # Mostrar el árbol de clientes
    print("Árbol de clientes:")
    sistema.imprimirClientes()
    #print()
    # Ingresar un vehículo
    #vehiculo3 = Vehiculo(idVehiculo="V003", placa="DEF456", ubicacion="Piso 3")
    #sistema.ingresarVehiculo("Juan Perez", vehiculo3)
    # Mostrar el árbol de clientes actualizado
    #print("Árbol de clientes actualizado:")
    #sistema.imprimirClientes()
    #print()

if __name__ == "__main__":
    main()