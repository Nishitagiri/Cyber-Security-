##import math
##
##
### Function to check prime number
##def is_prime(num):
##    if num <= 1:
##        return False
##
##    for i in range(2, int(math.sqrt(num))+1):
##        if num % i == 0:
##            return False
##
##    return True
##
##
### Generate RSA keys
##def generate_keys(p, q):
##
##    n = p * q
##
##    phi = (p-1)*(q-1)
##
##    e = 2
##
##    while e < phi:
##        if math.gcd(e, phi) == 1:
##            break
##        e += 1
##
##
##    d = pow(e, -1, phi)
##
##    return (e,n),(d,n)
##
##
##
### Encryption
##def encrypt(message, public_key):
##
##    e,n = public_key
##
##    encrypted = []
##
##    for char in message:
##        encrypted.append(pow(ord(char),e,n))
##
##    return encrypted
##
##
##
### Decryption
##def decrypt(cipher, private_key):
##
##    d,n = private_key
##
##    decrypted=""
##
##    for num in cipher:
##        decrypted += chr(pow(num,d,n))
##
##    return decrypted
##
##
##
### CLI Program
##
##print("RSA Encryption and Decryption")
##
##p=int(input("Enter prime number p: "))
##q=int(input("Enter prime number q: "))
##
##
##if not(is_prime(p) and is_prime(q)):
##    print("Numbers must be prime")
##
##else:
##
##    public,private = generate_keys(p,q)
##
##    print("\nPublic Key:",public)
##    print("Private Key:",private)
##
##
##    message=input("\nEnter message: ")
##
##    encrypted=encrypt(message,public)
##
##    print("\nEncrypted Message:")
##    print(encrypted)
##
##
##    decrypted=decrypt(encrypted,private)
##
##    print("\nDecrypted Message:")
##    print(decrypted)


#GUI
import tkinter as tk
from tkinter import messagebox
import math


def generate_keys():

    p=int(p_entry.get())
    q=int(q_entry.get())

    n=p*q

    phi=(p-1)*(q-1)

    e=2

    while e<phi:

        if math.gcd(e,phi)==1:
            break

        e+=1


    d=pow(e,-1,phi)

    public=(e,n)
    private=(d,n)

    public_entry.delete(0,tk.END)
    private_entry.delete(0,tk.END)

    public_entry.insert(0,str(public))
    private_entry.insert(0,str(private))


def encrypt():

    e,n=eval(public_entry.get())

    msg=message_entry.get()

    cipher=[]

    for ch in msg:
        cipher.append(pow(ord(ch),e,n))


    encrypted_entry.delete(0,tk.END)

    encrypted_entry.insert(0,str(cipher))



def decrypt():

    d,n=eval(private_entry.get())

    cipher=eval(encrypted_entry.get())

    text=""

    for num in cipher:

        text += chr(pow(num,d,n))


    decrypted_entry.delete(0,tk.END)

    decrypted_entry.insert(0,text)



window=tk.Tk()

window.title("RSA Encryption and Decryption '080")
window.geometry("500x500")


tk.Label(window,text="Prime Number p").pack()

p_entry=tk.Entry(window)
p_entry.pack()


tk.Label(window,text="Prime Number q").pack()

q_entry=tk.Entry(window)
q_entry.pack()



tk.Button(window,text="Generate Keys",
          command=generate_keys).pack(pady=10)



tk.Label(window,text="Public Key").pack()

public_entry=tk.Entry(window,width=50)
public_entry.pack()



tk.Label(window,text="Private Key").pack()

private_entry=tk.Entry(window,width=50)
private_entry.pack()



tk.Label(window,text="Message").pack()

message_entry=tk.Entry(window,width=50)
message_entry.pack()



tk.Button(window,text="Encrypt",
          command=encrypt).pack(pady=10)



tk.Label(window,text="Encrypted Text").pack()

encrypted_entry=tk.Entry(window,width=50)
encrypted_entry.pack()



tk.Button(window,text="Decrypt",
          command=decrypt).pack(pady=10)



tk.Label(window,text="Decrypted Message").pack()

decrypted_entry=tk.Entry(window,width=50)
decrypted_entry.pack()



window.mainloop()
