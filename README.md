# CS361

1. Instructions on How to Request Data from the Microservice:

The microservice is a python script which can be called with arguments via subprocesws calls or system calls.

Here is how to request data using the python library, os System calls.

The following is text in a python program that would call the script while passing it arguments:

```
import os
import subprocess
cwd = os.getcwd()
program = cwd + "/text_microservice.py"

#PROGRAM CODE
#PROGRAM CODE
#PROGRAM CODE

#Call to Microservice

result = subprocess.run(["python", program, "example.txt", "True"], capture_output=True, text=True)
print(result.stdout.strip())
```

2. Instructions on How to Request Data from the Microservice:

The the microservice will require the location of a text file. If the text file is in the same directory as the script, the script can find the file with just the file name.
The microservice can also optionally call another program that allows the user to edit a text file and save it. This option is optional and not required to call the microservice.

In order to request data from the microsercice when running the subprocess call replace in the above text where "example.txt" is written with the name of the desired text file's contents.

If you want the microservice to call the optional text editing program pass "True" as in the example above. If you do not need to run the text editing program you may exclude writing "True" and leave that argument blank.

The microservice will return the contents of the text file to the place where it was called like a function. Save the output of the microservice script to a variable such as the "result" above.

You may use and manipulate the contetnts of the text file as desired after.

Example of simple call to microservice that does not use the optional text editing service.

```
import os
import subprocess
cwd = os.getcwd()
program = cwd + "/text_microservice.py"

#PROGRAM CODE
#PROGRAM CODE
#PROGRAM CODE

#Call to Microservice

result = subprocess.run(["python", program, "example.txt"], capture_output=True, text=True)
#Code that manipulates text stored in result
```
![Text Replacement Program](https://github.com/Jay-JayG/CS361/assets/105891722/4d420c33-ad72-4fe3-a5ae-fe6d64cd088d)
