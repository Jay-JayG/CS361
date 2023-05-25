import sys
# before running this file, it is important to note that both this file as well as the text file you intend to search through
# must be inside the same folder, and the console must be opened to that specific folder otherwise the program will tell you
# that the file name you searched for doesn't exist.

def text_search():
    # ask user for name of input file
    fileName = input("Input name of text file to search in: ")
    searchFile = open(fileName, "r")

    # check if the file opens successfully
    if searchFile.closed:
        print("Error opening input file!")
        exit(); # use return instead?
    
    # read and close text file
    searchData = searchFile.read()
    searchFile.close()

    # ask user for text string to search for
    searchString = input("Input the string of text you wish to search for: ")

    # return search results
    if searchString in searchData:
        sys.stdout.write("Result(s) found!")
        return True
    else:
        sys.stdout.write("No results found.")
        return False


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python file_text_search.py <file_name> <search_term>")
        sys.exit(1)

    file_name = sys.argv[1]
    search_term = sys.argv[2]
    text_search(file_name, search_term)