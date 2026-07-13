###Design and implement algorithms to encrypt and decrypt messages using classical substitution techniques - CLI
##def encrypt(text, shift):
##    result = ""
##
##    for char in text:
##        if char.isalpha():
##            if char.isupper():
##                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
##            else:
##                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
##        else:
##            result += char
##
##    return result
##
##
##def decrypt(text, shift):
##    result = ""
##
##    for char in text:
##        if char.isalpha():
##            if char.isupper():
##                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
##            else:
##                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
##        else:
##            result += char
##
##    return result
##
##
##message = input("Enter Message: ")
##key = int(input("Enter Shift Key: "))
##
##encrypted = encrypt(message, key)
##decrypted = decrypt(encrypted, key)
##
##print("Encrypted Message:", encrypted)
##print("Decrypted Message:", decrypted)

###Design and implement algorithms to encrypt and decrypt messages using classical substitution techniques - GUI
##
##import tkinter as tk
##from tkinter import messagebox
##
##def encrypt():
##    text = message_entry.get("1.0", tk.END).strip()
##    if text == "":
##        messagebox.showwarning("Warning", "Please enter a message.")
##        return
##
##    try:
##        shift = int(key_entry.get())
##    except ValueError:
##        messagebox.showerror("Incorrect", "Please enter a valid numeric key.")
##        return
##
##    result = ""
##
##    for char in text:
##        if char.isalpha():
##            if char.isupper():
##                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
##            else:
##                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
##        else:
##            result += char
##
##    output_entry.config(state="normal")
##    output_entry.delete("1.0", tk.END)
##    output_entry.insert(tk.END, result)
##    output_entry.config(state="disabled")
##
##
##def decrypt():
##    text = message_entry.get("1.0", tk.END).strip()
##    if text == "":
##        messagebox.showwarning("Warning", "Please enter a message.")
##        return
##
##    try:
##        shift = int(key_entry.get())
##    except ValueError:
##        messagebox.showerror("Incorrect", "Please enter a valid numeric key.")
##        return
##
##    result = ""
##
##    for char in text:
##        if char.isalpha():
##            if char.isupper():
##                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
##            else:
##                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
##        else:
##            result += char
##
##    output_entry.config(state="normal")
##    output_entry.delete("1.0", tk.END)
##    output_entry.insert(tk.END, result)
##    output_entry.config(state="disabled")
##
##
### ---------------- Clear Function ----------------
##def clear():
##    message_entry.delete("1.0", tk.END)
##    key_entry.delete(0, tk.END)
##
##    output_entry.config(state="normal")
##    output_entry.delete("1.0", tk.END)
##    output_entry.config(state="disabled")
##
##
### ---------------- GUI ----------------
##root = tk.Tk()
##root.title("080 Caesar Cipher")
##root.geometry("500x450")
##root.configure(bg="#E8F0FE")
##
##title = tk.Label(
##    root,
##    text="Caesar Cipher Encryption & Decryption",
##    font=("Arial", 16, "bold"),
##    bg="#E8F0FE",
##    fg="green"
##)
##title.pack(pady=10)
##
###message
##tk.Label(root, text="Enter Message:", bg="#E8F0FE",
##         font=("Arial", 11, "bold")).pack()
##
##message_entry = tk.Text(root, height=5, width=45)
##message_entry.pack(pady=5)
##
###key
##tk.Label(root, text="Shift Key:", bg="#E8F0FE",
##         font=("Arial", 11, "bold")).pack()
##
##key_entry = tk.Entry(root, width=10, font=("Arial", 12))
##key_entry.pack(pady=5)
##
###buttons
##button_frame = tk.Frame(root, bg="#E8F0FE")
##button_frame.pack(pady=10)
##
##encrypt_btn = tk.Button(
##    button_frame,
##    text="Encrypt",
##    width=12,
##    bg="dark green",
##    fg="white",
##    command=encrypt
##)
##encrypt_btn.grid(row=0, column=0, padx=5)
##
##decrypt_btn = tk.Button(
##    button_frame,
##    text="Decrypt",
##    width=12,
##    bg="dark green",
##    fg="white",
##    command=decrypt
##)
##decrypt_btn.grid(row=0, column=1, padx=5)
##
##clear_btn = tk.Button(
##    button_frame,
##    text="Clear",
##    width=12,
##    bg="dark green",
##    fg="white",
##    command=clear
##)
##clear_btn.grid(row=0, column=2, padx=5)
##
###output
##tk.Label(root, text="Result:", bg="#E8F0FE",
##         font=("Arial", 11, "bold")).pack()
##
##output_entry = tk.Text(root, height=5, width=45, state="disabled")
##output_entry.pack(pady=5)
##
##root.mainloop()

###Design and implement algorithms to encrypt and decrypt messages using  transposition techniques - CLI
##def encrypt(text, key):
##    rail = [['\n' for i in range(len(text))]
##            for j in range(key)]
##
##    direction_down = False
##    row, col = 0, 0
##
##    for char in text:
##        if row == 0 or row == key - 1:
##            direction_down = not direction_down
##
##        rail[row][col] = char
##        col += 1
##
##        if direction_down:
##            row += 1
##        else:
##            row -= 1
##
##    result = ""
##    for i in range(key):
##        for j in range(len(text)):
##            if rail[i][j] != '\n':
##                result += rail[i][j]
##
##    return result
##
##
##def decrypt(cipher, key):
##    rail = [['\n' for i in range(len(cipher))]
##            for j in range(key)]
##
##    direction_down = None
##    row, col = 0, 0
##
##    for i in range(len(cipher)):
##        if row == 0:
##            direction_down = True
##        if row == key - 1:
##            direction_down = False
##
##        rail[row][col] = '*'
##        col += 1
##
##        if direction_down:
##            row += 1
##        else:
##            row -= 1
##
##    index = 0
##    for i in range(key):
##        for j in range(len(cipher)):
##            if rail[i][j] == '*' and index < len(cipher):
##                rail[i][j] = cipher[index]
##                index += 1
##
##    result = ""
##    row, col = 0, 0
##
##    for i in range(len(cipher)):
##        if row == 0:
##            direction_down = True
##        if row == key - 1:
##            direction_down = False
##
##        result += rail[row][col]
##        col += 1
##
##        if direction_down:
##            row += 1
##        else:
##            row -= 1
##
##    return result
##
##
##text = input("Enter Message: ")
##key = int(input("Enter Number of Rails: "))
##
##cipher = encrypt(text, key)
##print("Encrypted Message:", cipher)
##
##plain = decrypt(cipher, key)
##print("Decrypted Message:", plain)

#GUI

import tkinter as tk
from tkinter import messagebox


def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    result = ""

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        result += rail[row][col]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result


def encrypt_gui():
    text = message.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Enter a message")
        return

    try:
        key = int(key_entry.get())
        if key < 2:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter a valid rail number (>=2)")
        return

    result = encrypt(text, key)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    output.config(state="disabled")


def decrypt_gui():
    text = message.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Enter a message")
        return

    try:
        key = int(key_entry.get())
        if key < 2:
            raise ValueError
    except:
        messagebox.showerror("Error", "Enter a valid rail number (>=2)")
        return

    result = decrypt(text, key)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    output.config(state="disabled")


def clear():
    message.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.config(state="disabled")


root = tk.Tk()
root.title("080 Rail Fence Cipher")
root.geometry("520x470")
root.configure(bg="#EAF4FC")

title = tk.Label(root,
                 text="Rail Fence Cipher Encryption & Decryption",
                 font=("Arial", 16, "bold"),
                 bg="#EAF4FC",
                 fg="green")
title.pack(pady=10)

tk.Label(root,
         text="Enter Message",
         bg="#EAF4FC",
         font=("Arial",11,"bold")).pack()

message = tk.Text(root,height=5,width=50)
message.pack()

tk.Label(root,
         text="Number of Rails",
         bg="#EAF4FC",
         font=("Arial",11,"bold")).pack(pady=5)

key_entry = tk.Entry(root,font=("Arial",12),width=10)
key_entry.pack()

frame = tk.Frame(root,bg="#EAF4FC")
frame.pack(pady=12)

tk.Button(frame,
          text="Encrypt",
          width=12,
          bg="green",
          fg="white",
          command=encrypt_gui).grid(row=0,column=0,padx=5)

tk.Button(frame,
          text="Decrypt",
          width=12,
          bg="green",
          fg="white",
          command=decrypt_gui).grid(row=0,column=1,padx=5)

tk.Button(frame,
          text="Clear",
          width=12,
          bg="green",
          fg="white",
          command=clear).grid(row=0,column=2,padx=5)

tk.Label(root,
         text="Result",
         bg="#EAF4FC",
         font=("Arial",11,"bold")).pack()

output = tk.Text(root,height=5,width=50,state="disabled")
output.pack(pady=5)

root.mainloop()



