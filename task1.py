"""
1) Write a Python program using Function to which will do the following
   a) The function will create a text file with the current timestamp
   b) The file content should have the content of the current timestamp
"""
import datetime

#Defining function to create current timestamp
def create_timestamp_file():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the filename with the current timestamp
    filename = f"timestamp_{current_timestamp}.txt"
    
    # Write the current timestamp to the file
    with open(filename, 'w') as file:
        file.write(current_timestamp)
    file.close()

# Call the function to create the timestamp file
create_timestamp_file()























"""
2) Write another Python
"""