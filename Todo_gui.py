import functions
import FreeSimpleGUI as sg
import time
sg.theme("Black")
clock=sg.Text('',key='clock')
label = sg.Text("type in a todo")
input_box = sg.InputText(tooltip="enter todo",key='todo')
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key='todos',
                    enable_events=True, size=[45,10])
edit_button=sg.Button("Edit")
exit_button =sg.Button("Exit")
complete_button=sg.Button("Delete")
window=sg.Window('My Todo APP',
                 layout=[[clock],[label],
                         [input_box,add_button],
                         [list_box,edit_button,complete_button],
                         [exit_button]],
                 font=('Helvetica',20))
while True:
    event,values= window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b,%d,%Y%H:%M:%S"))
    print(values)

    match event:
        case"Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case"Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select item",font=('Helvetica',20))

        case "Delete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("please delete item",font=('Helvetica',20))

        case "Exit":
            break

        case'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()