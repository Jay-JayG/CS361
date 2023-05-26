import sys

# before running this file, it is important to note that both this file as well as the text file you intend to search through
# must be inside the same folder, and the console must be opened to that specific folder otherwise the program will tell you
# that the file name you searched for doesn't exist.

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Please provide 2 arguments.")
    sys.exit(1)

# file to search
fileName = sys.argv[1]

# text string to search for
searchString = sys.argv[2]

searchFile = open(fileName, "r")
# check if the file opens successfully
if searchFile.closed:
    print("Error opening input file!")
    exit()  # use return instead?

# read and close text file
searchData = searchFile.read()
searchFile.close()

# return search results
if searchString in searchData:
    sys.stdout.write("Result(s) found!")
else:
    sys.stdout.write("No results found.")
