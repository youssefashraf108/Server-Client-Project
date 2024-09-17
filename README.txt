Project 1: TCP Client-Server Application
Author: Youssef Abdeltawab
Class: 4310


#######################################################################
			HOW TO RUN
#######################################################################
1) Download server_tcp.py, client_tcp.py and database.txt on your computer
3) Transfer server_tcp.py on remote server on eros
4) Transfer client_tcp.py on remote server on zeus 
5) Transfer database.txt on remote server (You don't have to do this step, python progran can create database text automatically)
6) Once uploaded on the server, navigate to the directory where you saved the files. 
7) Run the server_tcp.py on eros server first 
8) python server_tcp.py
9) Run the client_tcp.py on zeus server second
10) python client_tcp.py
11) Once the program is running, menu option will be displayed and you can follow the commands. 
12) The server and client should be able to communicate with each other. 

Hint: in client_tcp if you have difficutly uploading files on the remote server, you can run the server
and client program on your local server. To do this:
1) Go to client program find line 9 to 10
2) uncomment the following code:

#to run on your local machine 
#hostname = socket.gethostbyname(socket.gethostname())

After this you should be able to run the code without needing to use eros or zeus remote server