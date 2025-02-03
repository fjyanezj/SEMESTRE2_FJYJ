import os
import subprocess
import datetime
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

HISTORIAL_PATH = "historial.txt"

def guardar_en_historial(ruta_script):
    """Guarda en un archivo el script ejecutado con fecha y hora."""
    with open(HISTORIAL_PATH, "a") as historial:
        historial.write(f"{datetime.datetime.now()} - {ruta_script}\n")

def mostrar_historial():
    """Muestra el historial de scripts ejecutados."""
    if not os.path.exists(HISTORIAL_PATH):
        print(Fore.YELLOW + "No hay historial disponible." + Style.RESET_ALL)
        return

    print(Fore.BLUE + "\n--- Historial de scripts ejecutados ---\n" + Style.RESET_ALL)
    with open(HISTORIAL_PATH, "r") as historial:
        print(historial.read())

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un script con numeración de líneas y colores."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, "r") as archivo:
            codigo = archivo.read()
            print(Fore.YELLOW + f"\n--- Código de {ruta_script} ---\n" + Style.RESET_ALL)
            for i, linea in enumerate(codigo.splitlines(), start=1):
                print(f"{Fore.CYAN}{i:4d}: {Style.RESET_ALL}{linea}")
            return codigo
    except FileNotFoundError:
        print(Fore.RED + "El archivo no se encontró." + Style.RESET_ALL)
        return None
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}" + Style.RESET_ALL)
        return None

def ejecutar_codigo(ruta_script):
    """Ejecuta un script en una nueva terminal."""
    try:
        if os.name == "nt":  # Windows
            subprocess.Popen(["cmd", "/k", "python", ruta_script])
        else:  # macOS y Linux
            subprocess.Popen(["gnome-terminal", "--", "python3", ruta_script])
        
        guardar_en_historial(ruta_script)
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al ejecutar el código: {e}" + Style.RESET_ALL)

def mostrar_menu():
    """Muestra el menú principal con unidades dinámicas y opciones adicionales."""
    ruta_base = os.getcwd()
    unidades = [d for d in os.listdir(ruta_base) if os.path.isdir(d)]

    while True:
        print(Fore.GREEN + "\nMenu Principal - Dashboard" + Style.RESET_ALL)
        for i, unidad in enumerate(unidades, start=1):
            print(f"{i} - {unidad}")
        print("9 - Ver historial de scripts ejecutados")
        print("0 - Salir")

        eleccion_unidad = input("Elige una opción: ")
        if eleccion_unidad == "0":
            print(Fore.BLUE + "Saliendo del programa." + Style.RESET_ALL)
            break
        elif eleccion_unidad == "9":
            mostrar_historial()
        else:
            try:
                eleccion_unidad = int(eleccion_unidad) - 1
                if 0 <= eleccion_unidad < len(unidades):
                    mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
                else:
                    print(Fore.RED + "Opción no válida." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

def mostrar_sub_menu(ruta_unidad):
    """Muestra el submenú con subcarpetas dentro de la unidad seleccionada."""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(Fore.MAGENTA + "\nSubmenú - Selecciona una subcarpeta" + Style.RESET_ALL)
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == "0":
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print(Fore.RED + "Opción no válida." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts .py dentro de la subcarpeta seleccionada."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith(".py")]

    while True:
        print(Fore.CYAN + "\nScripts - Selecciona un script para ver y ejecutar" + Style.RESET_ALL)
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == "0":
            break
        elif eleccion_script == "9":
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == "1":
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == "0":
                            print(Fore.BLUE + "No se ejecutó el script." + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "Opción no válida." + Style.RESET_ALL)
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print(Fore.RED + "Opción no válida." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Opción no válida." + Style.RESET_ALL)

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
