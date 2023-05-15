import os
import PySimpleGUI as pg
cwd = os.getcwd()

pg.theme("default1")
file_list_column = [
    [
        pg.Text("Folder"),
        pg.In(size=(30, 1), enable_events=True, key="-FOLDER-"),
        pg.FolderBrowse(),
    ],
    [
        pg.Listbox(
            values=[],
            enable_events=True,
            size=(50, 20),
            key="-FILE_LIST-"
        )
    ]
]

file_viewer_column = [
    [pg.Text("Choose a file from the list", size=(50, 1))],
    [pg.Text("File name: ", size=(70, 3), key="-TOUT-")],
    [pg.Multiline(size=(70, 30), key="-TEXT-")],
    [pg.Button("Save")]
]

layout = [
    [
        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.Column(file_viewer_column)
    ]
]

window = pg.Window("File Editor", layout, finalize=True)

folder_location = cwd

files = os.listdir(folder_location)
file_names = [
    file for file in files
    if os.path.isfile(os.path.join(folder_location, file)) and file.lower().endswith((".txt", ".py", ".cpp"))
]
window["-FILE_LIST-"].update(file_names)
while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == "Exit":
        break
    elif event == "-FOLDER-":
        folder_location = values["-FOLDER-"]
        try:
            files = os.listdir(folder_location)
        except:
            files = []

        file_names = [
            file for file in files
            if os.path.isfile(os.path.join(folder_location, file)) and file.lower().endswith((".txt", ".py", ".cpp"))
        ]
        window["-FILE_LIST-"].update(file_names)

    elif event == "-FILE_LIST-" and len(values["-FILE_LIST-"]) > 0:
        selected_file = values["-FILE_LIST-"][0]
        with open(os.path.join(folder_location, selected_file)) as file:
            lines = file.read()
            window["-TOUT-"].update(os.path.join(folder_location, selected_file))
            window["-TEXT-"].update(lines)
    elif event == "Save" and len(values["-FILE_LIST-"]) > 0:
        selected_file = values["-FILE_LIST-"][0]
        with open(os.path.join(folder_location, selected_file), 'w') as file:
            file.write(values["-TEXT-"])

window.close()
