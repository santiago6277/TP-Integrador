import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('DarkBlue3')

def build():

    layout1 = [
        [sg.Text('Infromación versión',font=(font_name,28))],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    layout2 = [
        [sg.Text('Acerca de',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Image("src/resources/images/provincia.png")],
        [sg.Text("""El elemento Tab es otro contenedor de elementos que permite organizar la ventana en pestañas.
Para agregar un elemento Tab a la ventana, se debe agregar un elemento TabGroup al layout de la ventana.
El elemento TabGroup recibe como parámetro un listado de elementos Tab.
Cada elemento Tab recibe como parámetro un listado de elementos que se mostrarán en la pestaña.
El elemento Image permite mostrar una imagen en la ventana.""")]
    ]

    layout = [
        [sg.Text('Versión 1.0')],
        [sg.HorizontalSeparator()],
        [sg.TabGroup([[sg.Tab('Infromación versión', layout1), sg.Tab('Acerca de', layout2)]])],
    ]

    window = sg.Window('Ejemplo de elemento tabs', layout, font=(font_name,font_size), modal=True)
    return window