import tkinter as tk
from tkinter import messagebox


def calculate_dh():
    try:
        # Get values from input fields
        p = int(p_entry.get())
        g = int(g_entry.get())
        a = int(a_entry.get())  # Private key of Simran
        b = int(b_entry.get())  # Private key of Riya

        if p <= 1:
            messagebox.showerror("Error", "p must be greater than 1.")
            return

        if g <= 0:
            messagebox.showerror("Error", "g must be positive.")
            return

        if a <= 0 or b <= 0:
            messagebox.showerror("Error", "Private keys must be positive.")
            return

        # Calculate public keys
        A = pow(g, a, p)
        B = pow(g, b, p)

        # Calculate shared secret keys
        key_simran = pow(B, a, p)
        key_riya = pow(A, b, p)

        # Display results
        simran_public_result.config(text=f"Simran's Public Key: {A}")
        riya_public_result.config(text=f"Riya's Public Key: {B}")

        simran_shared_result.config(
            text=f"Simran's Shared Key: {key_simran}"
        )

        riya_shared_result.config(
            text=f"Riya's Shared Key: {key_riya}"
        )

        # Check whether both keys are equal
        if key_simran == key_riya:
            status_result.config(
                text="✓ Key Exchange Successful!",
                fg="green"
            )
        else:
            status_result.config(
                text="✗ Key Exchange Failed!",
                fg="red"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid integer values."
        )


def clear_fields():
    p_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)
    a_entry.delete(0, tk.END)
    b_entry.delete(0, tk.END)

    simran_public_result.config(text="")
    riya_public_result.config(text="")
    simran_shared_result.config(text="")
    riya_shared_result.config(text="")
    status_result.config(text="")


# ---------------- GUI WINDOW ----------------

root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
root.geometry("650x650")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="Diffie-Hellman Key Exchange",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Secure Key Exchange over an Insecure Network",
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="#bbbbbb"
)
subtitle.pack(pady=(0, 20))


# ---------------- PARAMETERS ----------------

parameter_frame = tk.Frame(
    root,
    bg="#2b2b40",
    padx=25,
    pady=20
)
parameter_frame.pack(padx=30, fill="x")

tk.Label(
    parameter_frame,
    text="Public Parameters",
    font=("Arial", 14, "bold"),
    bg="#2b2b40",
    fg="#ffffff"
).grid(row=0, column=0, columnspan=2, pady=(0, 15))


# Prime number p
tk.Label(
    parameter_frame,
    text="Prime Number (p):",
    font=("Arial", 11),
    bg="#2b2b40",
    fg="white"
).grid(row=1, column=0, sticky="w", pady=8)

p_entry = tk.Entry(
    parameter_frame,
    width=30,
    font=("Arial", 11)
)
p_entry.grid(row=1, column=1, pady=8)


# Primitive root g
tk.Label(
    parameter_frame,
    text="Primitive Root (g):",
    font=("Arial", 11),
    bg="#2b2b40",
    fg="white"
).grid(row=2, column=0, sticky="w", pady=8)

g_entry = tk.Entry(
    parameter_frame,
    width=30,
    font=("Arial", 11)
)
g_entry.grid(row=2, column=1, pady=8)


# ---------------- PRIVATE KEYS ----------------

key_frame = tk.Frame(
    root,
    bg="#2b2b40",
    padx=25,
    pady=20
)
key_frame.pack(padx=30, pady=15, fill="x")

tk.Label(
    key_frame,
    text="Private Keys",
    font=("Arial", 14, "bold"),
    bg="#2b2b40",
    fg="white"
).grid(row=0, column=0, columnspan=2, pady=(0, 15))


# Simran private key
tk.Label(
    key_frame,
    text="Simran's Private Key:",
    font=("Arial", 11),
    bg="#2b2b40",
    fg="white"
).grid(row=1, column=0, sticky="w", pady=8)

a_entry = tk.Entry(
    key_frame,
    width=30,
    font=("Arial", 11)
)
a_entry.grid(row=1, column=1, pady=8)


# Riya private key
tk.Label(
    key_frame,
    text="Riya's Private Key:",
    font=("Arial", 11),
    bg="#2b2b40",
    fg="white"
).grid(row=2, column=0, sticky="w", pady=8)

b_entry = tk.Entry(
    key_frame,
    width=30,
    font=("Arial", 11)
)
b_entry.grid(row=2, column=1, pady=8)


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=15)

calculate_button = tk.Button(
    button_frame,
    text="Generate Shared Key",
    command=calculate_dh,
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10
)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 11, "bold"),
    bg="#d9534f",
    fg="white",
    padx=30,
    pady=10
)
clear_button.grid(row=0, column=1, padx=10)


# ---------------- RESULTS ----------------

result_frame = tk.Frame(
    root,
    bg="#2b2b40",
    padx=25,
    pady=15
)
result_frame.pack(padx=30, fill="x")

tk.Label(
    result_frame,
    text="Key Exchange Results",
    font=("Arial", 14, "bold"),
    bg="#2b2b40",
    fg="white"
).pack(pady=(0, 10))

simran_public_result = tk.Label(
    result_frame,
    text="",
    font=("Arial", 11),
    bg="#2b2b40",
    fg="#61dafb"
)
simran_public_result.pack(pady=3)

riya_public_result = tk.Label(
    result_frame,
    text="",
    font=("Arial", 11),
    bg="#2b2b40",
    fg="#61dafb"
)
riya_public_result.pack(pady=3)

simran_shared_result = tk.Label(
    result_frame,
    text="",
    font=("Arial", 11, "bold"),
    bg="#2b2b40",
    fg="#ffd700"
)
simran_shared_result.pack(pady=3)

riya_shared_result = tk.Label(
    result_frame,
    text="",
    font=("Arial", 11, "bold"),
    bg="#2b2b40",
    fg="#ffd700"
)
riya_shared_result.pack(pady=3)


# Status
status_result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f"
)
status_result.pack(pady=15)


root.mainloop()
