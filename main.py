from views.menu import menu_principal, menu_empleado, menu_departamento, menu_proyecto, menu_indicadores
from controllers.departamento_controller import DepartamentoController
from controllers.empleado_controller import EmpleadoController
from controllers.proyecto_controller import ProyectoController
from controllers.indicadores_controller import IndicadoresController
from models.departamento import Departamento
from models.empleado import Empleado
from models.proyecto import Proyecto
from models.indicadores import obtener_indicadores, obtener_indicador

departamento_controller = DepartamentoController()
empleado_controller = EmpleadoController()
proyecto_controller = ProyectoController()
indicadores_controller = IndicadoresController()


def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            while True:
                menu_empleado()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "1.1": 
                    nombre = input("Ingrese el nombre del empleado: ")
                    direccion = input("Ingrese la direccion del empleado: ")
                    telefono = input("Ingrese el telefono del empleado: ")
                    email = input("Ingrese el correo electrónico del empleado: ")
                    fecha_inicio = input("Ingrese la fecha de inicio del empleado: ")
                    salario = input("Ingrese el salario del empleado: ")
                    
                    print("Departamentos disponibles: ")
                    departamentos = departamento_controller.listar_departamentos()
                    for dep in departamentos:
                        print(f"ID: {dep[0]}, Nombre: {dep[1]}")
                    
                    departamento_id = input("Ingrese el ID del departamento al que pertenece el empleado (opcional): ")
                    departamento_id = int(departamento_id) if departamento_id else None
                    
                    while True:
                        departamento_id = input("Ingrese el ID del departamento al que pertenece el empleado (opcional): ")
                        if departamento_id:
                            departamento_id = int(departamento_id)
                            if departamento_controller.validar_id_departamento(departamento_id):
                                break  
                            else:
                                print(f"El ID de departamento {departamento_id} no es válido. Por favor, intente nuevamente.")
                        else:
                            departamento_id = None  
                            break  


                    rut =  input("Ingrese el rut del empleado: ")
                    
                    print ("Proyectos disponibles: ")
                    proyectos = proyecto_controller.listar_proyectos()
                    for pro in proyectos:
                        print(f"ID: {pro[0]}, Nombre: {pro[1]}")
                    
                    proyecto_id = input("Ingrese el ID del proyecto al que pertenece el empleado (opcional): ")
                    proyecto_id = int(proyecto_id) if proyecto_id else None
                    
                    while True:
                        proyecto_id = input("Ingrese el ID del proyecto al que pertenece el empleado (opcional): ")
                        if proyecto_id:
                            proyecto_id = int(proyecto_id)
                            if proyecto_controller.validar_id_proyecto(proyecto_id):
                                break  
                            else:
                                print(f"El ID de proyecto {proyecto_id} no es válido. Por favor, intente nuevamente.")
                        else:
                            proyecto_id = None  
                            break  

                    nuevo_empleado = Empleado(nombre=nombre, direccion=direccion,
                                              telefono=telefono, email=email, fecha_inicio=fecha_inicio,
                                              salario=salario, departamento_id=departamento_id, rut=rut, proyecto_id=proyecto_id)
                    empleado_controller.crear_empleado(nuevo_empleado)
                    print("Empleado creado exitosamente.")

                elif sub_opcion == "1.2": #listar empleado
                    empleados = empleado_controller.listar_empleados()
                    for emp in empleados:
                        print(emp)

                elif sub_opcion == "1.3": #buscar empleado
                    id_emp = int(input("Ingrese el ID del empleado a buscar: "))
                    empleado = empleado_controller.buscar_empleado_por_id(id_emp)
                    if empleado:
                        print(empleado)
                    else:
                        print("Empleado no encontrado.")

                elif sub_opcion == "1.4": #modificar empleado
                    id_emp = int(input("Ingrese el ID del empleado a modificar: "))
                    empleado = empleado_controller.buscar_empleado_por_id(id_emp)
                    if empleado:
                        nombre = str(input("Ingrese el nuevo nombre del empleado: "))
                        direccion = input("Ingrese la nueva direccion del empleado: ")
                        telefono = int(input("Ingrese el nuevo telefono del empleado: "))
                        email = input("Ingrese el nuevo correo electronico del empleado: ")
                        fecha_inicio = input("Ingrese la nueva fecha de inicio del empleado: ")
                        salario = input("Ingrese el nuevo salario del empleado: ")
                        print("Departamentos disponibles:")
                        departamentos = departamento_controller.listar_departamentos()
                        for dep in departamentos:
                            print(f"ID: {dep[0]}, Nombre: {dep[1]}")

                        nuevo_departamento_id = input("Ingrese el nuevo ID del departamento: ")
                        nuevo_departamento_id = int(nuevo_departamento_id)
                        rut = input("Ingrese el nuevo rut del empleado: ")
                        proyectos = proyecto_controller.listar_proyectos()
                        for pro in proyectos:
                            print(f"ID: {pro[0]}, Nombre: {pro[1]}")

                        nuevo_proyecto_id = input("Ingrese el nuevo ID del proyecto: ")
                        nuevo_proyecto_id = int(nuevo_proyecto_id)

                        empleado_modificado = Empleado(nombre=nombre, direccion=direccion,
                                              telefono=telefono, email=email, fecha_inicio=fecha_inicio,
                                              salario=salario, departamento_id=departamento_id, rut=rut)
                        empleado_controller.modificar_empleado(empleado_modificado)
                        print("Empleado modificado exitosamente.")
                    else:
                        print("Empleado no encontrado.")

                elif sub_opcion == "1.5": #eliminar empleado
                    id_emp = int(input("Ingrese el ID del empleado a eliminar: "))
                    empleado_controller.eliminar_empleado(id_emp)
                    print("Empleado eliminado exitosamente.")

                elif sub_opcion == "1.6": #volver al menu principal
                    break

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        elif opcion == "2":
            while True:
                menu_departamento()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "2.1":
                    nombre = input("Ingrese el nombre del departamento: ")
                    gerente_id = input("Ingrese el ID del gerente (opcional): ")
                    gerente_id = int(gerente_id) if gerente_id else None

                    nuevo_departamento = Departamento(nombre=nombre, gerente_id=gerente_id)
                    departamento_controller.crear_departamento(nuevo_departamento)
                    print("Departamento creado exitosamente.")

                elif sub_opcion == "2.2":
                    departamentos = departamento_controller.listar_departamentos()
                    for dep in departamentos:
                        print(dep)

                elif sub_opcion == "2.3":
                    id_dep = int(input("Ingrese el ID del departamento a buscar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        print(departamento)
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "2.4":
                    id_dep = int(input("Ingrese el ID del departamento a modificar: "))
                    departamento = departamento_controller.buscar_departamento_por_id(id_dep)
                    if departamento:
                        nombre = input("Ingrese el nuevo nombre del departamento: ")
                        gerente_id = input("Ingrese el nuevo ID del gerente (opcional): ")
                        gerente_id = int(gerente_id) if gerente_id else None

                        departamento_modificado = Departamento(id=id_dep, nombre=nombre, gerente_id=gerente_id)
                        departamento_controller.modificar_departamento(departamento_modificado)
                        print("Departamento modificado exitosamente.")
                    else:
                        print("Departamento no encontrado.")

                elif sub_opcion == "2.5":
                    id_dep = int(input("Ingrese el ID del departamento a eliminar: "))
                    departamento_controller.eliminar_departamento(id_dep)
                    print("Departamento eliminado exitosamente.")

                elif sub_opcion == "2.6":
                    break

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        elif opcion == "3":
            while True:
                menu_proyecto()
                sub_opcion = input("Seleccione una opción: ")
                
                if sub_opcion == "3.1":
                    nombre = input("Ingrese el nombre del proyecto: ")
                    descripcion = input("Ingrese una descripcion para el proyecto: ")
                    fecha = input("Ingrese la fecha del proyecto: ")

                    nuevo_proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha=fecha)
                    proyecto_controller.crear_proyecto(nuevo_proyecto)
                    print("Proyecto creado exitosamente.")

                elif sub_opcion == "3.2":
                    proyectos = proyecto_controller.listar_proyectos()
                    for pro in proyectos:
                        print(pro)

                elif sub_opcion == "3.3":
                    id_pro = int(input("Ingrese el ID del proyecto a buscar: "))
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        print(proyecto)
                    else:
                        print("Proyecto no encontrado.")

                elif sub_opcion == "3.4":
                    id_pro = int(input("Ingrese el ID del proyecto a modificar: "))
                    proyecto = proyecto_controller.buscar_proyecto_por_id(id_pro)
                    if proyecto:
                        nombre = input("Ingrese el nuevo nombre del proyecto: ")
                        descripcion = input("Ingrese la nueva descripcion del proyecto: ")
                        fecha = input("Ingrese la nueva fecha del proyecto: ")

                        proyecto_modificado = Proyecto(id=id_pro, nombre=nombre, descripcion=descripcion)
                        proyecto_controller.modificar_proyecto(proyecto_modificado)
                        print("Proyecto modificado exitosamente.")
                    else:
                        print("Proyecto no encontrado.")

                elif sub_opcion == "3.5":
                    id_pro = int(input("Ingrese el ID del proyecto a eliminar: "))
                    proyecto_controller.eliminar_proyecto(id_pro)
                    print("Proyecto eliminado exitosamente.")

                elif sub_opcion == "3.6":
                    empleados = empleado_controller.listar_empleados()
                    for emp in empleados:
                            print(f"ID: {emp[0]}, Nombre: {emp[1]}")

                    nuevo_empleado_id = input("Ingrese el nuevo ID del empleado: ")
                    nuevo_empleado_id = int(nuevo_empleado_id)

                elif sub_opcion == "3.7":
                    break

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        elif opcion == "4":  # Menú de indicadores
            while True:
                menu_indicadores()
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "4.1":  # Consultar un indicador específico
                    nombre = input("Ingrese el nombre del indicador a consultar: ").lower()
                    indicador = indicadores_controller.consultar_indicador(nombre)
                    print(indicador if indicador != "Indicador no encontrado." else "Indicador no encontrado.")

                elif sub_opcion == "4.2":  # Listar todos los indicadores
                    indicadores = indicadores_controller.listar_indicadores()
                    if indicadores:
                        print("Indicadores guardados:")
                        for ind in indicadores:
                            print(ind)
                    else:
                        print("No hay indicadores guardados.")

                elif sub_opcion == "4.3":  # Agregar un nuevo indicador
                    nombre = input("Ingrese el nombre del indicador: ").lower()
                    try:
                        valor_actual = float(input("Ingrese el valor actual del indicador: "))
                        indicadores_controller.agregar_indicador(nombre, valor_actual)
                        print(f"Indicador '{nombre}' guardado correctamente.")
                    except ValueError:
                        print("El valor ingresado no es válido. Intente nuevamente.")
                
                elif sub_opcion == "4.4":  # Volver al menú principal
                    print("Volviendo al menú principal...")
                    break

        elif opcion == "5":  # Salir del sistema
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intenta nuevamente.")

if __name__ == "__main__":
    main()