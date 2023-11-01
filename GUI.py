import tkinter as tk

def start_button_clicked():
    login = login_entry.get()
    password = password_entry.get()
    print(f"Login: {login}, Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Set the size of the window
root.geometry("400x300")

# Create and place the Login label and Entry field
login_label = tk.Label(root, text="Login:")
login_label.pack()

login_entry = tk.Entry(root)
login_entry.pack()

# Create and place the Password label and Entry field
password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")  # Show * for password input
password_entry.pack()

# Create and place the Start button
start_button = tk.Button(root, text="Start", command=start_button_clicked)
start_button.pack()

# Center all elements
for widget in [login_label, login_entry, password_label, password_entry, start_button]:
    widget.pack_configure(anchor="center")

# Run the Tkinter main loop
root.mainloop()
