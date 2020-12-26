import PySimpleGUI as sg
import sys

class InterfaceMaker:
    def __init__(self):
        pass

    def favorite_color_picker(self):
        choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

        layout = [[sg.Text('What is your favorite color?')],
                  [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
                  [sg.Button('Ok')]]

        window = sg.Window('Pick a color', layout)

        while True:  # the event loop
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Ok':
                if values['-COLOR-']:  # if something is highlighted in the list
                    sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
        window.close()

    def make_file_browser(self):
        if len(sys.argv) == 1:
            event, values = sg.Window('My Script',
                            [[sg.Text('Document to open')],
                            [sg.In(), sg.FileBrowse()],
                            [sg.Open(), sg.Cancel()]]).read(close=True)
            fname = values[0]
        else:
            fname = sys.argv[1]

        if not fname:
            sg.popup("Cancel", "No filename supplied")
            raise SystemExit("Cancelling: no filename supplied")
        else:
            sg.popup('The filename you chose was', fname)

    def make_responsive_interface(self):
        # Define the window's contents
        layout = [[sg.Text("What's your name?")],  # Part 2 - The Layout
                  [sg.Input()],
                  [sg.Button('Ok')]]

        # Create the window
        window = sg.Window('Window Title', layout)  # Part 3 - Window Defintion

        # Display and interact with the Window
        event, values = window.read()  # Part 4 - Event loop or Window.read call

        # Do something with the information gathered
        print('Hello', values[0], "! Thanks for trying PySimpleGUI")

        # Finish up by removing from the screen
        window.close()  # Part 5 - Close the Window

    def make_grid_using_math(self):
        layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]
        event, values = sg.Window('List Comprehensions', layout).read(close=True)

if __name__ == '__main__':
    gui = InterfaceMaker()
    gui.make_file_browser()
