import PySimpleGUI as sg

sg.theme('DarkTea16')
table_content = []
layout = [
    [sg.Table(
        headings = ['Observation', 'Result'], 
        values = table_content, 
        expand_x=True, 
        hide_vertical_scroll=True,
        key = '-TABLE-')],
    [sg.Input(key = '-INPUT-', expand_x = True), sg.Button('Submit')]
]

window = sg.Window('Graph App', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            table_content.append([len(table_content) + 1,float(new_value)])
            window['-TABLE-'].update(table_content)

window.close()