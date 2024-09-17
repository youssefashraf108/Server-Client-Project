import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ""  # Listen on any interface
PORT = 12035  # Use a specific port for communication
BUFFER_SIZE = 1024

# Function to display student's information by ID
def display_student_by_ID(student_id):
    # Open the database file in read mode
    with open('database.txt', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into a list of student information
            student = line.strip().split(',')
            # Check if the student ID matches the given ID
            if student[0] == student_id:
                # Return the student's information
                return f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Score: {student[3]}"
    # Return message if student is not found
    return "Student not found in the database."

# Function to add a new student's information to the database
def add_student(student_info):
    # Check if all fields are provided
    if len(student_info) != 4:  
        return "Invalid input. Please provide Student ID, First Name, Last Name, and Score."
    
    # Check if First Name and Last Name are not empty and contain only alphabetic characters
    if not student_info[1].isalpha() or not student_info[2].isalpha():
        return "Invalid input. First name and last name must be alphabetic."
    
    # Check if ID and Score are numeric
    if not student_info[0].isdigit() or not student_info[3].isdigit():
        return "Invalid input. Student ID and Score must be numeric."
    
    # Check if ID is a 6-digit number
    if len(student_info[0]) != 6:
        return "Invalid input. Student ID must be 6 digits long."
    
    # Write the new entry to the database file
    with open('database.txt', 'a') as file:
        file.write(','.join(student_info) + '\n')
    
    # Return success message
    return "Entry added to the database successfully."

# Function to display students' information with scores above a given score
def display_student_by_score(score):
    # List to store matching students
    matching_students = []
    # Open the database file in read mode
    with open('database.txt', 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into a list of student information
            student_info = line.strip().split(',')
            # Check if the student has a score higher than the given score
            if len(student_info) == 4 and int(student_info[3]) > int(score):
                # Add the student to the matching_students list
                matching_students.append(student_info)
    # Check if any students were found
    if matching_students:
        # Return formatted information of all matching students
        return "\n".join([f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Score: {student[3]}" for student in matching_students])
    else:
        # Return message if no students were found
        return "No students found in the database with a score above the given score."

# Function to delete a student from the database by ID
def delete_student_ID(student_id):
    # Read all lines from the database file
    with open('database.txt', 'r') as file:
        lines = file.readlines()
    # Flag to check if the entry was deleted
    deleted = False
    # Open the database file in write mode
    with open('database.txt', 'w') as file:
        # Iterate through each line in the file
        for line in lines:
            # Check if the student ID in the line matches the given ID
            if line.strip().split(',')[0] != student_id:
                # Write the line back to the file if the ID does not match
                file.write(line)
            else:
                # Set deleted flag to True if the ID matches
                deleted = True
    # Return appropriate message based on deletion status
    if deleted:
        return "Student information deleted successfully from the database."
    else:
        return "Student not found in the database."

# Function to display information of all students in the database
def display_all_students():
    # Open the database file in read mode
    with open('database.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
        # Check if any lines were read
        if lines:
            # Return formatted information of all students
            return "\n".join(lines)
        else:
            # Return message if the database is empty
            return "The database is empty. Use option 1 to add entries to the database."

# Main function to handle client-server communication
def main():

    
    print("Listening on port", PORT)
    # Bind the socket to the IP address and port
    server.bind((ip, PORT))
    # Listen for incoming connections
    server.listen(1)
    # Accept a connection from a client
    con, addr = server.accept()
    
    while True:
        # Receive data from the client
        data = con.recv(BUFFER_SIZE).decode('utf-8')
        if not data:
            break
        
        # Split received data into command and parameters (if any)
        command, *params = data.split()
        
        # Execute commands based on client requests
        if command == "add_student":
            response = add_student(tuple(params))
            print(response)

        elif command == "user_input_student_id":
            if len(params) > 0:
                response = display_student_by_ID(params[0])
                print(response)
            else:
                response = "Invalid request. No student ID provided"
                print(response)

        elif command == "show_student_score":
            response = display_student_by_score(int(params[0]))
            print(response)

        elif command == "show_all":
            response = display_all_students()
            print(response)

        elif command == "remove_student_by_id":
            response = delete_student_ID(params[0])
            print(response)
            
        elif command == "exit_program":
            response = "Goodbye!"
            print(response)
            break
        else:
            response = "Invalid command."
            print(response)
        
        # Send response back to the client
        con.send(response.encode('utf-8'))

    # Close the server socket
    server.close()

if __name__ == "__main__":
    main()
