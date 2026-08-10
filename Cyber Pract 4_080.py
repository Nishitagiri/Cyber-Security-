import tkinter as tk
import hashlib

# RSA values
p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = 2753

signature = None


def sign_message():
    global signature

    message = message_entry.get()

    if message == "":
        result.config(text="Please enter a message.", fg="red")
        return

    # Hash the message
    hash_value = int(
        hashlib.sha256(message.encode()).hexdigest(),
        16
    )

    # Create RSA signature
    signature = pow(hash_value, d, n)

    signature_label.config(
        text="Digital Signature: " + str(signature)
    )

    result.config(
        text="Digital Signature Created Successfully!",
        fg="green"
    )


def verify_message():
    if signature is None:
        result.config(
            text="Create a signature first!",
            fg="red"
        )
        return

    message = verify_entry.get()

    if message == "":
        result.config(
            text="Please enter a message to verify.",
            fg="red"
        )
        return

    # Hash the entered message
    hash_value = int(
        hashlib.sha256(message.encode()).hexdigest(),
        16
    )

    # Verify using public key
    verified_hash = pow(signature, e, n)

    if verified_hash == hash_value % n:
        result.config(
            text="Signature Verified!\n"
                 "Message is authentic and not modified.",
            fg="green"
        )
    else:
        result.config(
            text="Verification Failed!\n"
                 "Message has been modified.",
            fg="red"
        )


def clear():
    global signature

    signature = None

    message_entry.delete(0, tk.END)
    verify_entry.delete(0, tk.END)

    signature_label.config(text="")
    result.config(text="")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("RSA Digital Signature")
root.geometry("600x450")


title = tk.Label(
    root,
    text="RSA DIGITAL SIGNATURE",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)


tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12)
).pack()

message_entry = tk.Entry(
    root,
    width=55,
    font=("Arial", 12)
)
message_entry.pack(pady=10)


tk.Button(
    root,
    text="Create Digital Signature",
    command=sign_message,
    font=("Arial", 11),
    bg="purple",
    fg="white"
).pack(pady=10)


signature_label = tk.Label(
    root,
    text="",
    font=("Arial", 10)
)
signature_label.pack(pady=10)


tk.Label(
    root,
    text="Enter Message for Verification:",
    font=("Arial", 12)
).pack(pady=10)

verify_entry = tk.Entry(
    root,
    width=55,
    font=("Arial", 12)
)
verify_entry.pack(pady=10)


tk.Button(
    root,
    text="Verify Signature",
    command=verify_message,
    font=("Arial", 11),
    bg="green",
    fg="white"
).pack(pady=10)


tk.Button(
    root,
    text="Clear",
    command=clear
).pack(pady=5)


result = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
result.pack(pady=20)


root.mainloop()
