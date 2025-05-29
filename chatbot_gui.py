import tkinter as tk
from tkinter import scrolledtext

# Rule-based response function
def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ['hi', 'hello', 'hey']:
        return "Hello there! How can I help you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created with Python."
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great!"
    
    elif "help" in user_input:
        return "I can respond to greetings and simple questions."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

# Function to send message
def send_message():
    user_msg = user_entry.get()
    if user_msg.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_msg + "\n")
    response = get_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    user_entry.delete(0, tk.END)

# Create GUI window
window = tk.Tk()
window.title("Simple Chatbot")

# Chat display area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)
chat_area.config(state=tk.NORMAL)

# Entry box
user_entry = tk.Entry(window, width=40, font=("Arial", 12))
user_entry.pack(padx=10, pady=5, side=tk.LEFT)

# Send button
send_button = tk.Button(window, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(padx=5, pady=5, side=tk.LEFT)

# Run the app
window.mainloop()
