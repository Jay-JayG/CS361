import subprocess

script_path = 'C:/Users/Joel/Documents/2023_spring/cs361/CS361/file_text_search.py'

file_name = "card1.txt"
search_term = "text"
command = ['python', script_path, file_name, search_term]
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
