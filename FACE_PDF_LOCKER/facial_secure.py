import tkinter as tk
from tkinter import filedialog, messagebox
import os
import cv2
import pickle
import numpy as np

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import pikepdf
import face_recognition_models
import face_recognition

# CRYPTO FUNCTIONS
def generate_aes_key():
    return get_random_bytes(32)

def encrypt_pdf(input_pdf, output_enc, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(input_pdf, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(pad(data, AES.block_size))

    with open(output_enc, "wb") as f:
        f.write(iv + encrypted)

def decrypt_pdf(enc_file, output_pdf, key):
    with open(enc_file, "rb") as f:
        data = f.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_pdf, "wb") as f:
        f.write(decrypted)

# FACE FUNCTIONS
def register_face(face_file, status_callback):
    cap = cv2.VideoCapture(0)
    status_callback("Press SPACE to capture face")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Register Face", frame)
        key = cv2.waitKey(1)

        if key == 32:
            break
        elif key == 27:
            cap.release()
            cv2.destroyAllWindows()
            return False
    cap.release()
    cv2.destroyAllWindows()

    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    encodings = face_recognition.face_encodings(rgb)
    if not encodings:
        raise Exception("No face detected")

    with open(face_file, "wb") as f:
        pickle.dump(encodings[0], f)
    return True

def verify_face(face_file, status_callback):
    with open(face_file, "rb") as f:
        known_face = pickle.load(f)

    cap = cv2.VideoCapture(0)
    status_callback("Verifying face...")

    for _ in range(25):
        ret, frame = cap.read()

        small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        encodings = face_recognition.face_encodings(rgb)
        if encodings:
            match = face_recognition.compare_faces(
                [known_face], encodings[0], tolerance=0.45
            )[0]

            cap.release()
            cv2.destroyAllWindows()
            return match

    cap.release()
    cv2.destroyAllWindows()
    return False

# GUI APP
class SecurePDFVault:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure PDF Vault")
        self.root.geometry("420x360")
        self.root.resizable(False, False)

        tk.Label(root, text="Secure PDF Vault",
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.status = tk.Label(root, text="Select a PDF", fg="blue")
        self.status.pack(pady=5)

        tk.Button(root, text="Select PDF",
                  command=self.select_pdf).pack(pady=5)

        tk.Button(root, text="Register Face",
                  command=self.register_face).pack(pady=5)

        tk.Button(root, text="Lock (Encrypt PDF)",
                  command=self.lock_pdf).pack(pady=5)

        tk.Button(root, text="Unlock (Decrypt PDF)",
                  command=self.unlock_pdf).pack(pady=5)

        tk.Button(root, text="Exit",
                  command=root.quit).pack(pady=10)

        self.pdf_path = None

    def update_status(self, msg):
        self.status.config(text=msg)
        self.root.update_idletasks()

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf"),
                ("Encrypted PDF Files", "*.enc")]
        )
        if self.pdf_path:
            self.update_status(os.path.basename(self.pdf_path))

    def register_face(self):
        if not self.pdf_path:
            messagebox.showerror("Error", "Select a PDF first")
            return

        face_file = self.pdf_path + ".face"
        try:
            register_face(face_file, self.update_status)
            messagebox.showinfo("Success", "Face registered")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def lock_pdf(self):
        if not self.pdf_path:
            messagebox.showerror("Error", "Select a PDF first")
            return

        face_file = self.pdf_path + ".face"
        if not os.path.exists(face_file):
            messagebox.showerror("Error", "Register face first")
            return

        key = generate_aes_key()
        enc_file = self.pdf_path + ".enc"
        key_file = self.pdf_path + ".key"

        encrypt_pdf(self.pdf_path, enc_file, key)

        with open(key_file, "wb") as f:
            f.write(key)

        os.remove(self.pdf_path)

        messagebox.showinfo("Locked", "PDF encrypted and locked")

    def unlock_pdf(self):
        if not self.pdf_path:
            messagebox.showerror("Error", "Select encrypted PDF")
            return

        face_file = self.pdf_path.replace(".enc", "") + ".face"
        key_file = self.pdf_path.replace(".enc", "") + ".key"

        if not verify_face(face_file, self.update_status):
            messagebox.showerror("Denied", "Face verification failed")
            return

        with open(key_file, "rb") as f:
            key = f.read()

        output_pdf = self.pdf_path.replace(".enc", "_unlocked.pdf")
        decrypt_pdf(self.pdf_path, output_pdf, key)

        messagebox.showinfo("Success", "PDF decrypted successfully")
# MAIN

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurePDFVault(root)
    root.mainloop()
