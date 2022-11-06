import PySimpleGUI as sg
from src.consts.font import font_name, font_size


sg.theme('DarkBlue3')

def build():

    reparticiones = [ "MSALGP", "MSGP", "ICULGP", "MAMGP", "MTGP"]
    
    layout = [
        [sg.Text('Ingresar expediente',font=(font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text('EX', size=(10,1)), sg.Input(size=(6,1),key='-EX-')],
        [sg.Text('Ano', size=(10,1)), sg.Input(size=(6,1),key='-Ano-')],
        [sg.Text('Numero', size=(10,1)), sg.Input(size=(13,1),key='-Numero-')],
        [sg.Text('GDEBA', size=(10,1)), sg.Input(size=(6,1),key='-GDEBA-')],
        [sg.Text('Reparticion', size=(15,1)), sg.Combo(reparticiones,default_value=reparticiones[0],size=(24,1),key="-Reparticion-",readonly=True)],
        [sg.Button('Guardar', size=(10, 1),key="-GUARDAR-", bind_return_key=True)]
    ]

    window = sg.Window('Ingresar expediente', layout, font=(font_name,font_size), modal=True)
    return window