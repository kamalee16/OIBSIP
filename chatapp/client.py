import socket
import threading
import tkinter as tk
from encryption import decrypt_message

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
username = input("Enter your name: ")


def receive():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            msg = decrypt_message(encrypted_msg)
            chat_box.insert(tk.END, msg + "\n")
        except:
            break

def send():
    message = entry.get()
    full_message = f"{username}: {message}"
    client.send(full_message.encode())
    entry.delete(0, tk.END)


window = tk.Tk()
window.title("Advanced Chat App")

chat_box = tk.Text(window, height=20, width=50)
chat_box.pack()

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT)

send_btn = tk.Button(window, text="Send", command=send)
send_btn.pack(side=tk.RIGHT)

threading.Thread(target=receive, daemon=True).start()
window.mainloop()
