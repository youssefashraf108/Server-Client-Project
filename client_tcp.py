import socket

# Create a TCP socket for communication.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the local machine.
#running on eros server 
hostname = "eros.cs.txstate.edu"
#to run on your local machine 
#hostname = socket.gethostbyname(socket.gethostname())
    
# Set the server's port number and buffer size for data transmission.
PORT = 12035
BUFFER_SIZE = 1024
HEADER = 64 

# Connect to the server using the socket and specified port.
client.connect((hostname, PORT))
FORMAT = 'utf-8'

def send(msg):
    message = msg.encode(FORMAT) 
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)




def main():
 
    
    # Start a loop to display menu options and interact with the server.
    while True:
        print("")
        print("*********************************************")
        print("*            MENU OPTIONS                    *")
        print("*********************************************")
        print("1. Add new student information to the database")
        print("2. Display student information by ID")
        print("3. Display student information by score")
        print("4. Display information of all students")
        print("5. Delete student entry by ID")
        print("6. Exit program")
        
        # Get user input for menu selection.
        UserInput = input("Enter your choice (1-6): ")
        
        # Process user input and prepare the request to send to the server.
        if UserInput == "1":
            Student_ID = input("Enter student ID: ")
            First_Name = input("Enter student first name: ")
            Last_Name = input("Enter student last name: ")
            score = input("Enter student score: ")
            user_request = f"add_student {Student_ID} {First_Name} {Last_Name} {score}"
        elif UserInput == "2":
            id = input("Enter student ID: ")
            user_request = f"user_input_student_id {id}"
        elif UserInput == "3":
            score = input("Enter score: ")
            user_request = f"show_student_score {score}"
        elif UserInput == "4":
            user_request = "show_all"
        elif UserInput == "5":
            id = input("Enter student ID to delete: ")
            user_request = f"remove_student_by_id {id}"
        elif UserInput == "6":
            user_request = "exit_program"
            client.send(user_request.encode('utf-8'))
            break
        else:
            print("Your choice was incorrect, please try again!")
            continue
        
        # Send the user request to the server.
        client.send(user_request.encode('utf-8'))
        
        # Receive and display the server's response.
        server_response = client.recv(BUFFER_SIZE).decode('utf-8')
        print("Server Response:", server_response)

    # Close the client socket.
    client.close()
    

if __name__ == "__main__":
    main()
