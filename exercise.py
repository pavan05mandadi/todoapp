import FreeSimpleGUI as sg

label1= sg.Text("Enter feet:")
input1=sg.Input(key="feet")


label2= sg.Text("Enter Inches:")
input2=sg.Input(key="inch")

convert_button =sg.Button("convert")
output_label=sg.Text("",key='output')
window=sg.Window("convertor",
                 layout=[[label1,input1],
                         [label2, input2] ,[convert_button,output_label]])


while True:
    event,values=window.read()
    feet=float(values["feet"])
    inch=float(values["inch"])
    meters = feet * 0.3048 + inch * 0.0254

    window["output"].update(value=meters)


window.close()