import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_expediente, nueva_ventana1
from src.handlers import ingresar_expediente_handler


def start():
    """
    Lanza la ejecución de la ventana
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    sg.theme('SystemDefault')

    window = pantalla_principal.build()
    window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente_handler.leer_archivo())

    while True:
        event, values = window.read()
        print(event)

        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-INGRESAR_EXPEDIENTE-':
            ingresar_expediente.start()
            window["-TABLA_EXPEDIENTE-"].update(ingresar_expediente_handler.leer_archivo())

        elif event == 'Información':
            nueva_ventana1.start()
        
        elif event == "Eliminar seleccion" and window["-TABLA_EXPEDIENTE-"].get():
            if values["-TABLA_EXPEDIENTE-"]:
                print(f'Fila selecciona de la tabla: {values["-TABLA_EXPEDIENTE-"][0]}')
                expediente_seleccionado = window["-TABLA_EXPEDIENTE-"].get()[values["-TABLA_EXPEDIENTE-"][0]]
                print(expediente_seleccionado)
        
        else:
            sg.popup("La aplicación se encuentra actualizada", title="Aviso")

    return window

