import PySimpleGUI as sg

layout = [
    [sg.Text("Select a Deck to begin Reviewing Cards",
    justification='center')],
    [sg.Text("Deck 1: 14 Cards", justification='center')],
    [sg.Text("Deck 2: 15 Cards", justification='center')],
    [sg.Text("Deck 3: 16 Cards", justification='center')],
    [sg.Text("Deck 4: 1 Card", justification='center')],
    [sg.Button("Create Deck"), sg.Button("Create Card")],
    [sg.Button("View All Cards")]
]

window = sg.Window(title="hello", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Create Deck":
        text = sg.popup_get_text('Enter Deck Name', title="New Deck")
        print(text)