# Secure Chat Application

## Objective
To develop a secure client-server chat application that allows multiple users to communicate in real time using encrypted messages and a simple graphical user interface.

## Steps Performed
- Implemented a server using Python socket programming to handle client connections.
- Created a client application with a Tkinter-based GUI for chatting.
- Used multithreading to enable simultaneous message sending and receiving.
- Added message encryption and decryption using Fernet symmetric encryption.
- Integrated an SQLite database to store user credentials and chat messages.
- Implemented message broadcasting so all connected clients receive messages securely.

## Tools Used
- Python  
- Socket Programming  
- Threading  
- Tkinter (GUI)  
- SQLite (Database)  
- Cryptography (Fernet Encryption)

## Steps to Run the Application
1. Install the required dependency:
   pip install cryptography
2. Run the server:
   python server.py
3. Open a new terminal and run the client:
   python client.py
4. Enter a username when prompted.
5. Run client.py in multiple terminals to connect multiple users.

## Outcome
A secure and functional chat application was successfully developed, enabling real-time encrypted communication between multiple clients with a simple graphical interface and database support.
