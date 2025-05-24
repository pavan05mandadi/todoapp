import FreeSimpleGUI as sg

layout = [
    [sg.Listbox(values=['Apple', 'Banana', 'Cherry'],
                key='fruit',
                size=(20, 3),
                )],
    [sg.Text("", key='output')]
]

window = sg.Window("Fruits", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'fruit':
        selected = values['fruit'][0]  # Listbox returns a list
        window['output'].update(f"You selected: {selected}")