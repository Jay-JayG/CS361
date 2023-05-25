import sys
import os

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Please provide 1-2 arguments.")
    sys.exit(1)

file_path = sys.argv[1]

if len(sys.argv) == 3:
    open_text_editor = sys.argv[2]
else:
    open_text_editor = False

if open_text_editor:
    cwd = os.getcwd()
    script_path = cwd + '/text_editing_program.py'
    result = os.system('python "{}" "{}"'.format(script_path, file_path))

with open(file_path, "r") as file:
    contents = file.read()
    sys.stdout.write(contents)
