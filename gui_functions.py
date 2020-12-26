import PySimpleGUI as pgui


layout = [[pgui.Text("common functions are..")],
          [pgui.Button("ok")],]

window = pgui.Window("common functions", layout)

while True:
    event, values = window.read()
    if event == "ok" or event == pgui.WIN_CLOSED:
        break

window.close()
