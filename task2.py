"""
2) Write another Python function to read from a text file.The function will take the name of 
the text file and display the content of the file into the console
"""

# Defining  a function named read_file that takes parameter file_name that represents the name of the file to be read
def read_file(file_name):

    # Open the file in read mode using a context manager (with statement)
    with open (file_name,"r") as file:
        # Read the content of the file and store it in the variable content
        content=file.read()
        # Print the content of the file
        print(content)

# Call the read_file function with the filename "text.txt"
read_file("text.txt")    
