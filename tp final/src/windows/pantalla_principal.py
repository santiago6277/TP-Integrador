from datetime import date
import PySimpleGUI as sg
from src.consts import font


def build():
    """
    Construye la ventana principal
    """
    # El theme siempre hay que ponerlo primero, sino no funciona
    sg.theme('DarkBlue3')

    font16 = ("Calibri Italic", 16)

    menu_def = [['&Archivo', ['!&Abrir', '&Guardar::guardarkey', '---', 'E&xit']],
            ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Actualizaciones', ['&Información']],
            ['&Ayuda', '&Acerca de...'], ]

    layout = [
        [sg.Menu(menu_def)],
        [sg.Text(f'Tareas pendientes {date.today().strftime("%d/%m/%Y")}', font=(font.font_name, 20), size=(30, 1))],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar expediente", key='-INGRESAR_EXPEDIENTE-', tooltip='Permite ingresar un expediente nuevo',
                      font=(font.font_name, 11))
        ],
        [sg.Table(values=[["-", "-", "-", "-", "-", "-"]], key="-TABLA_EXPEDIENTE-",
                  justification="c",
                  headings=[" EX ", "     Ano     ", "   Numero   ", " GDEBA ", " Reparticion "],
                  row_height=20, num_rows=10, header_background_color="#FF8000", right_click_menu=[[],["Eliminar seleccion"]])],
        [sg.Text("""La tabla superior guardará los expedientes a tramitar en la jornada.""")],
        
            ]
    window = sg.Window('Buzón de tareas v1.0', layout=layout, resizable=True, finalize=True)

    return window
