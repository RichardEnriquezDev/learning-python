
####### AGENDA PERSONAL #######

tareas = []
def mostrar_menu ():
    print("1. Agregar Tarea.")
    print("2. Ver tarea.")
    print("3. Marcar tarea como hecha.")
    print("4. Eliminar tarea.")
    print("5. Guardar tarea.")
    print("6. Salir.")

def ver_tareas():
    if not tareas:
        print("No hay tareas cargadas.")
        return

    print("\nLista de tareas: ")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔" if tarea[1] else " "
        print(f"({i}) [{estado}] {tarea[0]}")

def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    
    ver_tareas()
    numero = int(input("Ingrese el número de la tarea a eliminar: "))
    indice = int(numero) - 1
    tarea = tareas[indice]
    confirmar = input(f"¿Eliminar '{tarea}'? (s/n): ")
        
    if confirmar.lower() == "s": 
        tareas.pop(indice)
        print("Tarea eliminada.")
    else:
        print("Operación cancelada.")

def marcar_tarea():
    if not tareas:
        print("No hay tareas para marcar.")
        return
    ver_tareas()
    numero = int(input("Ingrese el número de la tarea a marcar: "))
    indice = numero - 1
    tareas[indice][1] = True

def guardar_tareas():
    with open("prácticas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea[0]}|{tarea[1]}\n")

def cargar_tareas():
    try:
        with open("prácticas.txt", "r") as archivo:
            for linea in archivo:
                texto, estado = linea.strip() .split("|")
                tareas.append([texto, estado == "True"])
        print("Tareas cargadas correctamnete.")
    except FileNotFoundError:
        pass

cargar_tareas()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        tarea = input("Ingrese una nueva tarea: ")
        tareas.append([tarea, False])
        print("Tarea agregada correctamente.")
    
    elif opcion == "2":
        ver_tareas()
    
    elif opcion == "3":
        marcar_tarea()

    elif opcion == "4":
        eliminar_tarea()
    
    elif opcion == "5":
        guardar_tareas()
        print("Tarea guardada. Saliendo del programa.")
        break
    
    elif opcion == "6":
        print("Saliendo del programa")
        break
    else:
        print("Opción inválida.")