
import FreeSimpleGUI as sg
label = sg.Text("type in a todo")
input_box = sg.InputText(tooltip="enter todo")
add_button=sg.Button("Add")
window=sg.Window('My Todo APP', layout=[[label],[input_box,add_button]])
window.read()
window.close()