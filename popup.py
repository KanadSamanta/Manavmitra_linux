import os
import subprocess
import sys

try:
    import PySimpleGUI as SG
except ModuleNotFoundError:
    os.system("pip3 install PySimpleGUI")
    import PySimpleGUI as SG

print("hello")
# Part 1 - The import
popup_to_show = open(os.path.join(sys.path[0], "error_massege.txt"), 'r')
massege = popup_to_show.read()
popup_to_show.close()
button_to_show = open(os.path.join(sys.path[0], "error_massege_button.txt"), 'r')
massege_button = button_to_show.read()
button_to_show.close()
# Define the window's contents
command_to_run = open(os.path.join(sys.path[0], "instruction.txt"), 'r')
instruction = command_to_run.read()
command_to_run.close()

layout = [[SG.Text(massege)], [SG.Button(massege_button)], [SG.Button('Exit')],
          [SG.Button('Copy')], button_to_show]  # Part 2 - The Layout

# Create the window
window = SG.Window('Window Title', layout)  # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()  # Part 4 - Event loop or Window.read call

# Do something with the information gathered
if 'ok' not in massege_button:
    if event == massege_button:
        os.system(instruction)
        sys.exit()
elif event == 'Copy':
    try:
        import pyperclip
    except ModuleNotFoundError:
        os.system("pip3 install pyperclip")

        import pyperclip
    pyperclip.copy(massege)


elif event == 'Exit' or event == SG.WIN_CLOSED:
    print("closeing")
    window.close()
else:
    print('hello')
# Finish up by removing from the screen
