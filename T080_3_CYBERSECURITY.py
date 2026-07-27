#---------------- code ----------------
import hmac
import hashlib

#function to generate mac
def generate_mac(message, secret_key):
    mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return mac

#function to verify mac
def verify_mac(message, secret_key, received_mac):
    generated_mac = generate_mac(message, secret_key)

    #secure comparison
    if hmac.compare_digest(generated_mac, received_mac):
        return True
    else:
        return False


message = input("Enter the message: ")
secret_key = input("Enter the secret key: ")

#generate mac
mac = generate_mac(message, secret_key)

print("\n'080 Generated MAC:")
print(mac)

#verification
print("\n--- '080 MAC Verification ---")
received_mac = input("Enter the MAC to verify: ")

if verify_mac(message, secret_key, received_mac):
    print(" '080 MAC Verified Successfully!")
    print("Data Integrity and Authenticity are Confirmed.")
else:
    print(" '080 MAC Verification Failed!")
    print("Message may have been modified or the key is incorrect.")


#---------------- GUI ----------------

import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib

#generating mac
def generate_mac():
    message = message_entry.get("1.0", tk.END).strip()
    secret_key = key_entry.get().strip()

    if not message or not secret_key:
        messagebox.showerror("Error", "Please enter both Message and Secret Key.")
        return

    mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, mac)


#verifying mac
def verify_mac():
    message = message_entry.get("1.0", tk.END).strip()
    secret_key = key_entry.get().strip()
    received_mac = verify_entry.get().strip()

    if not message or not secret_key or not received_mac:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    generated_mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(generated_mac, received_mac):
        result_label.config(
            text="MAC Verified Successfully!\nData Integrity & Authenticity Confirmed.",
            fg="green"
        )
    else:
        result_label.config(
            text="MAC Verification Failed!\nMessage or Key is Incorrect.",
            fg="red"
        )


#gui window
root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("600x500")
root.configure(bg="#EAF4FC")

title = tk.Label(
    root,
    text="Message Authentication Code (MAC)",
    font=("Arial", 18, "bold"),
    bg="#EAF4FC",
    fg="#003366"
)
title.pack(pady=15)

#message
tk.Label(root, text="Enter Message:", font=("Arial", 12),
         bg="#EAF4FC").pack(anchor="w", padx=20)

message_entry = tk.Text(root, height=5, width=60)
message_entry.pack(padx=20, pady=5)

#secret key
tk.Label(root, text="Secret Key:", font=("Arial", 12),
         bg="#EAF4FC").pack(anchor="w", padx=20)

key_entry = tk.Entry(root, width=50, show="*")
key_entry.pack(padx=20, pady=5)

#generate button
generate_btn = tk.Button(
    root,
    text="Generate '080 MAC",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=generate_mac
)
generate_btn.pack(pady=10)

#generated mac
tk.Label(root, text="Generated '080 MAC:", font=("Arial", 12),
         bg="#EAF4FC").pack(anchor="w", padx=20)

mac_entry = tk.Entry(root, width=80)
mac_entry.pack(padx=20, pady=5)

#verification
tk.Label(root, text="Enter '080 MAC to Verify:", font=("Arial", 12),
         bg="#EAF4FC").pack(anchor="w", padx=20)

verify_entry = tk.Entry(root, width=80)
verify_entry.pack(padx=20, pady=5)

#verify button
verify_btn = tk.Button(
    root,
    text="Verify '080 MAC",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    command=verify_mac
)
verify_btn.pack(pady=15)

#result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#EAF4FC"
)
result_label.pack(pady=10)

root.mainloop()

