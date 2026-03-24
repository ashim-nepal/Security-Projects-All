import tkinter as tk
from tkinter import filedialog, messagebox
import os, json, base64, hashlib
from datetime import datetime

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


LOGS_FILE = "audit_logs.log"



def audit_log(evnt):
    prv_hash = "0"
    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, "r") as f:
            lines = f.readlines()
            if lines:
                prv_hash = lines[-1].strip().split("|")[-1]

    timestamp = datetime.now().isoformat()
    record = f"{timestamp} | {evnt} | {prv_hash}"
    record_hash = hashlib.sha256(record.encode()).hexdigest()

    with open(LOGS_FILE, "a") as f:
        f.write(f"{record} | {record_hash}\n")

def load_public_key():
    return RSA.import_key(open("public.pem", "rb").read())

def load_private_key():
    return RSA.import_key(open("private.pem", "rb").read())

class SecurePDF:
    def __init__(self, root):
        self.root = root
        root.title("Secure PDF Vault")
        root.geometry("480x420")
        root.resizable(False, False)

        tk.Label(root, text="Secure PDF Vault",
                 font=("Helvetica", 16, "bold")).pack(pady=10)

        tk.Button(root, text="Select PDF",
                  command=self.select_pdf).pack(pady=5)

        self.file_label = tk.Label(root, text="No PDF selected", fg="red")
        self.file_label.pack()

        tk.Label(root, text="Encryption Password").pack(pady=(15, 0))
        self.password_entry = tk.Entry(root, show="*", width=30)
        self.password_entry.pack()

        tk.Button(root, text="Encrypt PDF",
                  command=self.encrypt_pdf).pack(pady=15)

        tk.Button(root, text="Decrypt PDF",
                  command=self.decrypt_pdf).pack(pady=5)

        self.file_path = None
        audit_log("APPLICATION_STARTED")
    
    def select_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"),("Encrypted Files","*.secure")])

        if self.file_path:
            self.file_label.config(
                    text=os.path.basename(self.file_path), fg="green")



    def encrypt_pdf(self):
        if not self.file_path or not self.file_path.endswith(".pdf"):
            messagebox.showerror("Error", "Select a pdf file")
            return

        password = self.password_entry.get()
        if len(password) < 8:
            messagebox.showerror("Error", "Password Too Weak")
            return

        audit_log("ENCRYPT_REQUEST")

        with open(self.file_path, "rb") as f:
            pdf_data = f.read()

        aes_key= get_random_bytes(32)

        cipher = AES.new(aes_key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(pdf_data)

        rsa_cipher = PKCS1_OAEP.new(load_public_key())
        encrypted_key = rsa_cipher.encrypt(aes_key)

        # Password hardening
        salt = get_random_bytes(16)
        pwd_key = PBKDF2(password, salt, dkLen=32, count=200000)

        package = {
            "ciphertext": base64.b64encode(ciphertext).decode(),
            "nonce": base64.b64encode(cipher.nonce).decode(),
            "tag": base64.b64encode(tag).decode(),
            "encrypted_key": base64.b64encode(encrypted_key).decode(),
            "salt": base64.b64encode(salt).decode()
        }

        save_path = self.file_path + ".secure"
        with open(save_path, "w") as f:
            json.dump(package, f)

        audit_log("ENCRYPT_SUCCESS")

        self.reset_ui()
        messagebox.showinfo("Success", "PDF encrypted successfully")


    def decrypt_pdf(self):
        if not self.file_path or not self.file_path.endswith(".secure"):
            messagebox.showerror("Error", "Select a .secure file")
            return

        password = self.password_entry.get()
        audit_log("DECRYPT_REQUEST")

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)

            rsa_cipher = PKCS1_OAEP.new(load_private_key())
            aes_key = rsa_cipher.decrypt(
                base64.b64decode(data["encrypted_key"])
            )

            cipher = AES.new(
                aes_key,
                AES.MODE_GCM,
                nonce=base64.b64decode(data["nonce"])
            )

            pdf_data = cipher.decrypt_and_verify(
                base64.b64decode(data["ciphertext"]),
                base64.b64decode(data["tag"])
            )

            out_path = "decrypted.pdf"
            with open(out_path, "wb") as f:
                f.write(pdf_data)

            audit_log("DECRYPT_SUCCESS")
            self.reset_ui()

            messagebox.showinfo("Success", "PDF decrypted as decrypted.pdf")

        except Exception:
            audit_log("DECRYPT_FAILED")
            messagebox.showerror("Error", "Decryption failed")


    def reset_ui(self):
        self.password_entry.delete(0, tk.END)
        self.file_label.config(text="No PDF selected", fg="red")
        self.file_path = None


if __name__ == "__main__":
    root = tk.Tk()
    SecurePDF(root)
    root.mainloop()

